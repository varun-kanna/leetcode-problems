class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        HashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i
