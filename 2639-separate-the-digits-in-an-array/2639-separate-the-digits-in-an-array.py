class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_str = ""
        for i in nums:
            nums_str += str(i)
        print(nums_str)
        final_list = []
        for j in range(len(nums_str)):
            final_list.append(int(nums_str[j]))
        print(final_list)
        return final_list
