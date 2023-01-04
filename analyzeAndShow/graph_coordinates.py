from __future__ import annotations

from itertools import combinations
from multiprocessing import Pool
from typing import List, Callable, Tuple

import pandas as pd
from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway
from scipy.spatial.distance import euclidean

from analyzeAndShow.constants_mysql import languages
from analyzeAndShow.word_metrics import functions_dict

data_filename = "translations.csv.xz"

translations_df = pd.read_csv(data_filename, index_col=0)


def send_to_graphstream(method: str):
    gateway = JavaGateway()
    app = JavaGateway().entry_point
    java_method = getattr(app, method)

    def inner(fun: Callable):
        def decorator_fun(*args, **kwargs):
            (edges_df, nodes_df) = fun(*args, **kwargs)
            args_list_edges = [ListConverter().convert(edges_df[col], gateway._gateway_client) for col in edges_df.columns]
            args_list_nodes = [ListConverter().convert(nodes_df[col], gateway._gateway_client) for col in nodes_df.columns]
            java_method(*args_list_edges, *args_list_nodes)

        return decorator_fun

    return inner


@send_to_graphstream('showGraph')
def get_graph_coords(languages: List[str] | str = None, categories: List[str] | str = None, node_type: str = "lang", metric: str = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Function calculating metrics, averaging them and returning graph edges with their length
    :param languages: list of languages to include in calculations
    :param categories: list of categories to include in calculations
    :param node_type: whether graph should present differences between categories or languages (default)
    :param metric: metric used
    :return:
    """
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
    # assert len(languages if node_type == "lang" else categories) <= 20  # visibility

    metric_fun = functions_dict[metric]
    reduced_df = translations_df[languages].loc[categories]
    iter_lang = ((reduced_df[lang1], reduced_df[lang2]) for lang1, lang2 in combinations(languages, 2))

    with Pool(24) as pool:
        lang_res = pool.starmap(metric_fun, iter_lang)
    dist_df = pd.DataFrame(data=lang_res, index=list(combinations(languages, 2)), columns=reduced_df.index).T

    if node_type == "lang":
        stats_df = dist_df.apply(['mean'], axis=0).T
    else:
        mean_dist_df = dist_df.groupby(level=0).agg(['mean'])
        stats_df = pd.DataFrame.from_dict({(cat1, cat2): euclidean(mean_dist_df.loc[cat1], mean_dist_df.loc[cat2]) for cat1, cat2 in combinations(categories, 2)}, orient="index", columns=['mean'])
        stats_df.index = pd.MultiIndex.from_tuples(list(stats_df.index), names=('label_0', 'label_1'))

    stats_df.reset_index(inplace=True)
    stats_df.columns = "label_0 label_1 mean".split()

    nodes = languages if node_type == "lang" else categories
    closeness_dict = {node: (len(nodes) - 1) / stats_df["mean"][(stats_df["label_0"] == node) | (stats_df["label_1"] == node) ].sum() for node in nodes}
    closeness_df = pd.Series(closeness_dict, name="closeness").rename_axis(index='label').reset_index()
    return stats_df, closeness_df


if __name__ == "__main__":
    get_graph_coords(languages="English Polish German".split(), categories="ANIMALS WEATHER TIME".split(), node_type="lang", metric="Levenshtein")
    get_graph_coords(languages=languages, categories="all", node_type="lang", metric="Levenshtein")
