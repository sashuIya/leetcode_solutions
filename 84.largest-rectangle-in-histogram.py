# Problem statement:
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/84.largest-rectangle-in-histogram.png

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # (w, h)
        res = 0
        heights.append(0)
        for end_h in heights:
            length = 0
            while s and s[-1][1] >= end_h:
                w, h = s[-1]
                length += w
                res = max(res, length * h)
                s.pop()
            
            s.append((length + 1, end_h))

        return res