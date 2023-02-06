# https://leetcode.com/problems/edit-distance

def minDistanceRecursive(n, m, word1, word2, res):
    if n < 0 and m < 0: return 0
    if n < 0: return m + 1
    if m < 0: return n + 1

    if (n, m) not in res:
        if word1[n] == word2[m]:
            res[(n, m)] = minDistanceRecursive(n - 1, m - 1, word1, word2, res)
        else:
            res[(n, m)] = 1 + min(minDistanceRecursive(n - 1, m - 1, word1, word2, res),
                                  minDistanceRecursive(n - 1, m, word1, word2, res), 
                                  minDistanceRecursive(n, m - 1, word1, word2, res))

    return res[(n, m)]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = dict()
        return minDistanceRecursive(len(word1) - 1, len(word2) - 1, word1, word2, res)
