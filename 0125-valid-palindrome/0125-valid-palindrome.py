class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        # left = 0
        # right = len(s)-1
        # i = 0
        # while i < int(len(s) / 2):
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #         i += 1
        #     else:
        #         return False
        # return True