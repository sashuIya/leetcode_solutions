class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1, 2, 2]

        digit = 1
        count_index = 2
        for index in range(n):
            count = s[count_index]
            s.extend([digit] * count)   

            digit = 2 if digit == 1 else 1
            count_index += 1

            if len(s) >= n:
                break

        result = 0
        for index in range(n):
            if s[index] == 1:
                result += 1

        return result
