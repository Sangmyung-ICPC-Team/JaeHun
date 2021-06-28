class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i, n in enumerate(nums):
            if n in result:
                return[i, result[n]]
            else:
                result[target - n] = i
