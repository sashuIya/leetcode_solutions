class Solution(object):
    def canReorderPositiveDoubled(self, A):
        count = {}
        for value in A:
            if not value in count:
                count[value] = 1
            else:
                count[value] += 1

        for value in A:
            if count[value] > 0:
                count[value] -= 1
                if not value * 2 in count or count[value * 2] == 0:
                    return False

                count[value * 2] -= 1

        return True


    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        negative_a = []
        non_negative_a = []

        for value in A:
            if value < 0:
                negative_a.append(-value)
            else:
                non_negative_a.append(value)

        
        negative_a = sorted(negative_a)
        non_negative_a = sorted(non_negative_a)

        return (self.canReorderPositiveDoubled(negative_a) and
                self.canReorderPositiveDoubled(non_negative_a))
