class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        threshold1, threshold2 = float("inf"), float("inf")
        for num in nums:
            if num <= threshold1:
                threshold1 = num
            elif num <= threshold2:
                threshold2 = num
            else:
                return True
        return False
        