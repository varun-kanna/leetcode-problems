class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.strip() == "":
            return True
        import string
        s = s.translate(str.maketrans("","", string.punctuation)).replace(" ", "").lower()
        if s[::-1] == s:
            return True
        else:
            return False
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