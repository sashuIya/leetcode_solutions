class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        count_by_value = {}
        for value in nums1:
            if value not in count_by_value:
                count_by_value[value] = 1
            else:
                count_by_value[value] += 1
        
        result = []
        for value in nums2:
            if value in count_by_value and count_by_value[value] > 0:
                result.append(value)
                count_by_value[value] -= 1
        
        return result;

