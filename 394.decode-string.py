# https://leetcode.com/problems/decode-string


# Stack solution.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [(1, [])]  # (number of repeats, string)
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + ord(c) - ord('0')
            elif c == '[':
                stack.append((k, []))
                k = 0
            elif c == ']':
                x, t = stack.pop()
                t = t * x
                stack[-1][1].extend(t)
            else:
                stack[-1][1].append(c)

        return ''.join(stack[0][1])

# Recursive solution.
def decodeStringRecursive(k, l, s):
    """ Returns a tuple (result for string that starts
                                         at index `l`,
                         index of the next `]`)
    """
    t = []
    next_k = 0
    i = l
    while i < len(s):
        c = s[i]

        if c.isdigit():
            next_k = next_k *10 + ord(c) - ord('0')
        elif c == '[':
            w, i = decodeStringRecursive(next_k, i + 1, s)
            t.extend(w)
            next_k = 0
        elif c == ']':
            return (t * k, i)
        else:
            t.append(c)

        i += 1
    
    return (t * k, i)

class Solution:
    def decodeString(self, s: str) -> str:
        return ''.join(decodeStringRecursive(1, 0, s)[0])