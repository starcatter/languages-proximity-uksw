from __future__ import annotations

from itertools import combinations
from multiprocessing import Pool
from typing import List

import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

from analyzeAndShow.word_metrics import functions_dict

data_filename = "translations.csv.xz"

translations_df = pd.read_csv(data_filename, index_col=0)


def get_graph_coords(languages: List[str] | str = None, categories: List[str] | str = None, node_type: str = "lang", metric: str = None) -> np.ndarray:
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
        categories = translations_df.columns.tolist()
    assert len(languages) >= 2
    assert len(categories) >= 1
    assert all((c in translations_df.index for c in categories))
    assert all((j in translations_df.columns for j in languages))
    assert metric in functions_dict
    assert node_type in ("lang", "cat")

    metric_fun = functions_dict[metric]
    reduced_df = translations_df[languages].loc[categories]

    with Pool(24) as pool:
        lang_res = pool.starmap(metric_fun, iter(((reduced_df[lang1], reduced_df[lang2]) for lang1, lang2 in combinations(languages, 2))))
    dist_df = pd.DataFrame(data=lang_res, index=list(combinations(languages, 2)), columns=reduced_df.index).T

    if node_type == "lang":
        stats_df = dist_df.apply(['mean'], axis=0).T.reset_index()
    else:
        mean_dist_df = dist_df.groupby(level=0).agg(['mean'])
        stats_df = pd.DataFrame.from_dict({(cat1, cat2): euclidean(mean_dist_df.loc[cat1], mean_dist_df.loc[cat2]) for cat1, cat2 in combinations(categories, 2)}, orient="index", columns=['mean'])
        stats_df.index = pd.MultiIndex.from_tuples(list(stats_df.index), names=('level0', 'level1'))

    return stats_df.reset_index().values


if __name__ == "__main__":
    graph_edges = get_graph_coords(categories="ANIMALS WEATHER TIME".split(), node_type="lang", languages="English Polish German".split(), metric="Levenshtein")
    print(graph_edges)
