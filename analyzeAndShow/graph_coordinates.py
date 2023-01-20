from __future__ import annotations

import copy
import glob
import os
from itertools import combinations, starmap
from multiprocessing import Pool
from typing import List, Any

import pandas as pd
from pandas import DataFrame
from scipy.spatial.distance import euclidean

from analyzeAndShow.word_metrics import functions_dict

data_filename = os.path.join(os.path.dirname(__file__),"translations.csv.xz")

translations_df = pd.read_csv(data_filename, index_col=0)



jar_path = glob.glob(os.path.join(os.path.dirname(__file__), "../displayInGraphStream/target/*dependencies.jar"), recursive=True)[0]

import jnius_config

jnius_config.set_classpath(".", jar_path)
from jnius import autoclass, detach


def _send_to_graphstream(edges_df, nodes_df, agg_labels, display=False, screen_shot=True):
    PyImportable = autoclass("org.uksw.akelm.WordGraph")
    classInst = PyImportable(display, screen_shot)
    java_meth = classInst.showGraph
    Double = autoclass('java.lang.Double')

    args_list_edges = [edges_df[col].tolist() if edges_df.dtypes[col] == object else list(map(Double, edges_df[col].tolist())) for col in edges_df.columns]
    args_list_nodes = [nodes_df[col].tolist() if nodes_df.dtypes[col] == object else list(map(Double, nodes_df[col].tolist())) for col in nodes_df.columns]
    java_meth(*args_list_edges, *args_list_nodes, agg_labels)
    detach()


def _get_graph_coords(languages: List[str] | str = None, categories: List[str] | str = None, node_type: str = "lang", metric: str = None, n_cpu=1) -> tuple[
    DataFrame | Any, DataFrame, list[str] | list[Any]]:
    """
    Function calculating metrics, averaging them and returning graph edges with their length
    :param languages: list of languages to include in calculations
    :param categories: list of categories to include in calculations
    :param node_type: whether graph should present differences between categories or languages (default)
    :param metric: metric used
    :return:
    """
    categories_in = copy.deepcopy(categories)
    languages_in = copy.deepcopy(languages)
    if categories == "all":
        categories = list(set(translations_df.index))
    if isinstance(categories, str):
        categories = [categories]
    if languages == "all":
        languages = translations_df.columns.tolist()
    languages = list(set(languages))
    categories = list(set(categories))
    assert len(languages) >= 2
    assert len(categories) >= 1
    assert all((c in translations_df.index for c in categories))
    assert all((j in translations_df.columns for j in languages))
    assert metric in functions_dict
    assert node_type in ("lang", "cat")

    metric_fun = functions_dict[metric]
    reduced_df = translations_df[languages].loc[categories]
    iter_lang = ((reduced_df[lang1], reduced_df[lang2]) for lang1, lang2 in combinations(languages, 2))

    if n_cpu == 1:
        lang_res = list(starmap(metric_fun, iter_lang))
    else:
        with Pool(n_cpu) as pool:
            lang_res = pool.starmap(metric_fun, iter_lang)
    dist_df = pd.DataFrame(data=lang_res, index=list(combinations(languages, 2)), columns=reduced_df.index).T.astype('double')

    if node_type == "lang":
        stats_df = dist_df.apply(['mean'], axis=0).T
        agg_labels = [categories_in] if categories_in == "all" else categories
    else:
        agg_labels = [languages_in] if languages_in == "all" else languages
        mean_dist_df = dist_df.groupby(level=0).agg(['mean'])
        stats_df = pd.DataFrame.from_dict({(cat1, cat2): euclidean(mean_dist_df.loc[cat1], mean_dist_df.loc[cat2]) for cat1, cat2 in combinations(categories, 2)}, orient="index", columns=['mean'])
        stats_df.index = pd.MultiIndex.from_tuples(list(stats_df.index), names=('label_0', 'label_1'))

    stats_df.reset_index(inplace=True)
    stats_df.columns = "label_0 label_1 mean".split()

    nodes = languages if node_type == "lang" else categories
    closeness_dict = {node: (len(nodes) - 1) / stats_df["mean"][(stats_df["label_0"] == node) | (stats_df["label_1"] == node)].sum() for node in nodes}
    closeness_df = pd.Series(closeness_dict, name="closeness").rename_axis(index='label').reset_index()
    return stats_df, closeness_df, agg_labels


def produce_graph(languages: List[str] | str = None, categories: List[str] | str = None, node_type: str = "lang", metric: str = None, n_cpu=1, display=False, print_screen=True):
    stats_df, closeness_df, agg_labels = _get_graph_coords(languages, categories, node_type, metric, n_cpu)
    _send_to_graphstream(stats_df, closeness_df, agg_labels, display, print_screen)
