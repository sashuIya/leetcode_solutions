# https://leetcode.com/problems/regular-expression-matching/

def isMatchRecursive(n, m, s, p, res):
    if n < 0 and m < 0: return True
    if m < 0: return False

    if (n, m) not in res:
        # n<0 doesn't mean False. Example: s="" (n is -1)  p="a*a*"
        if n < 0:
            if p[m] != '*': return False
            else:
                res[(n, m)] = isMatchRecursive(n, m - 2, s, p, res)
                return res[(n, m)] 
        
        # n >= 0 and m >= 0
        if s[n] == p[m] or p[m] == '.':
            res[(n, m)] = isMatchRecursive(n - 1, m - 1, s, p, res)
        elif p[m] == '*':
            res[(n, m)] = isMatchRecursive(n, m - 2, s, p, res)
            if p[m - 1] == s[n] or p[m - 1] == '.':
                res[(n, m)] = res[(n, m)] or isMatchRecursive(n - 1, m, s, p, res)
                # res[(n, m)] = res[(n, m)] or isMatchRecursive(n - 1, m - 2, s, p, res)
        else:
            res[(n, m)] = False
    
    return res[(n, m)]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = dict()
        return isMatchRecursive(len(s) - 1, len(p) - 1, s, p, res)
