class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for x in nums:
            t=[]
            while x>0:
                t.insert(0,x%10)
                x=x//10
            res+=t
        return res