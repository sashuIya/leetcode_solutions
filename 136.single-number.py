# Problem statement
# https://leetcode.com/problems/single-number/

"""
xor:
    Z_2 in every radix

    1, 1 -> 0
    0, 0 -> 0
    1, 0 -> 1
    0, 1 -> 1

Properties:
    1. A xor A = 0
    2. A xor B = B xor A
    3. (A xor B) xor C = A xor (B xor C)
    4. A xor 0 = A

Example:
    a =       101001
    a =       101001
    a xor a = 000000

    a =       101001
    b =       100101
    a xor b = 001100
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return nums[0] ^ nums[1] ^ ... ^ nums[-1]

        xor = 0
        for v in nums:
            xor = xor ^ v

        return xor