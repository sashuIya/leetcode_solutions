# https://leetcode.com/problems/longest-valid-parentheses

# 2023:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        res = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(':
                continue
            
            if s[i - 1] == '(':
                # This is a case '<VALID_BLOCK>()'. 
                # The result is 2+length(VALID_BLOCK).

                res[i] = 2
                # plus the length of VALID_BLOCK (if it exists).
                # VALID_BLOCK ends on symbol i-2.
                if i >= 2: res[i] += res[i - 2]
            elif res[i - 1] != i and s[i - 1 - res[i - 1]] == '(':
                # This is a case '<VALID_BLOCK_1>(<VALID_BLOCK_2>)'. 
                #                                ^               ^
                #                           i-1-res[i-1]         i
                # Result is `2 + length(VALID_BLOCK_1) + length(VALID_BLOCK_2)`.

                # Here we compute 2 + length(VALID_BLOCK_2)
                res[i] = res[i - 1] + 2

                # and then add length(VALID_BLOCK_1) (if applicable).
                if i - res[i] >= 0:
                    res[i] += res[i - res[i]]
            else:
                # This is a case ')<SOME_VALID_BLOCK>)'. Result is 0.
                pass
        
        return max(res)


## Another solution (from 2021):
def f(s, c1, c2):
    balance = 0
    result = 0
    local_result = 0
    for c in s:
        if c == c1:
            balance += 1
        if c == c2:
            if balance > 0:
                balance -= 1
                local_result += 1
                if balance == 0:
                    result = max(result, local_result)
            else:
                local_result = 0
                balance = 0

    return result * 2

class SolutionOld:
    def longestValidParentheses(self, s: str) -> int:
        return max(f(s, '(', ')'), f(s[::-1], ')', '('))
