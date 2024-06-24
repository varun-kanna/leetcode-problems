from ast import List


# Time Complexity: O(n^2) Space Complexity O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    count += 1
        return count


# Time Complexity: O(n) Space Complexity O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myCount = {}
        for i in nums:
            if i not in myCount:
                myCount[i] = 0
            myCount[i] += 1

        c = 0
        for v in myCount.values():
            c += (v * (v - 1)) // 2
        return c
