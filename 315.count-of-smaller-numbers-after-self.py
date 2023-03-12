# https://leetcode.com/problems/count-of-smaller-numbers-after-self

class SegmentTree:
    def __init__(self, n):
        k = 0
        while 2**k < n:
            k += 1
        
        self.array_size = 2**k
        self.offset = self.array_size - 1
        self.size = self.array_size + self.offset
        self.array = [0] * self.size
    
    def update(self, i, v):
        i += self.offset
        self.array[i] = v
        while i != 0:
            i = (i - 1) // 2
            self.array[i] = self.array[i*2 + 1] + self.array[i*2 + 2]
    
    def get_sum_recursive(self, v, l, r, L):
        if L > r: return 0

        if l >= L: return self.array[v]

        return (self.get_sum_recursive(2*v+1, l, (l+r)//2, L) +
                self.get_sum_recursive(2*v+2, (l+r)//2 + 1, r, L))

    def get_sum(self, i):
        return self.get_sum_recursive(0, 0, self.array_size - 1, i)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        array = []
        for i, v in enumerate(nums):
            array.append((v, i))
        
        array.sort()

        res = [0] * len(nums)

        st = SegmentTree(len(nums))
        for v, i in array:
            res[i] = st.get_sum(i + 1)
            st.update(i, 1)
        
        return res