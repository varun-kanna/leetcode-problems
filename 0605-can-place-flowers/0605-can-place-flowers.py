class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # This requires extra memory since we make a new array, O(n) space complexity
        # f = [0] + flowerbed + [0]
        # for i in range(1, len(f) - 1):
        #     if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
        #         f[i] = 1
        #         n -= 1
        # return n <= 0

        # This requires no additonal space, so constant O(1) space complexity
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0