class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0 
        sign = -1
        for i in range(len(str(n))):
            sign *= -1
            sum += (sign * int(str(n)[i]))
            print(sum)
        return sum