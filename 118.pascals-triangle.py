class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        Cnk = [[1]]
        for n in range(1, numRows):
            row = [1]
            for k in range(1, n):
                row.append(Cnk[n - 1][k - 1] + Cnk[n - 1][k])
            row.append(1)
            Cnk.append(row)

        return Cnk

