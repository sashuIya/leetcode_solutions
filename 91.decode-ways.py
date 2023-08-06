# Problem statement:
# https://leetcode.com/problems/decode-ways

# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/91.decode-ways.png

# A. Iterative solution
def iterative_solution(s: str) -> int:
    res = [0] * (len(s) + 2)
    res[len(s)] = 1
    res[len(s) + 1] = 0

    for k in range(len(s) - 1, -1, -1):
        if int(s[k]) == 0:
            res[k] = 0
        elif k + 1 <= len(s) and int(s[k:k+2]) > 26:
            res[k] = res[k + 1]
        else:
            res[k] = res[k + 1] + res[k + 2]

    return res[0]

# B. Recursive solution:
def f(k, s, res):
    if k == len(s):
        return 1
    
    if k not in res:
        res[k] = 0
        if s[k] != '0':
            res[k] += f(k + 1, s, res)
        if k + 1 < len(s) and (10 <= int(s[k:k+2]) <= 26):
            res[k] += f(k + 2, s, res)
        
    return res[k]

class Solution:
    def numDecodings(self, s: str) -> int:
        res = dict()
        return f(0, s, res)
        
        # or
        #return iterative_solution(s)
