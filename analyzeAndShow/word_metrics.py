import numpy as np
from strsimpy.levenshtein import Levenshtein
from strsimpy.cosine import Cosine
from strsimpy.longest_common_subsequence import LongestCommonSubsequence
from strsimpy.jaccard import Jaccard

functions_dict = {
"Levenshtein" :np.vectorize(Levenshtein().distance),
"LCS" : np.vectorize(LongestCommonSubsequence().distance),
"Cosine": np.vectorize(Cosine(1).distance),
"Jaccard": np.vectorize(Jaccard(1).distance),
}
