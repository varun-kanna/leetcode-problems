class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        import math
        def gcd(m,n):
            while m%n != 0:
                oldm = m
                oldn = n

                m = oldn
                n = oldm%oldn
            return n

        max_len = gcd(len(str1), len(str2))
        return str1[:max_len] if str1 + str2 == str2 + str1  else ""
       