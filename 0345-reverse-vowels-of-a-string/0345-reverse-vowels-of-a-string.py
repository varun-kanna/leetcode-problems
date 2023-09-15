class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O" , "U"]
        # list_words = [str(word) for word in s]
        # print(list_words)

        # left, right = 0, len(list_words) - 1

        # while left <= right:
        #     if list_words[right] not in vowels:
        #         right -= 1
        #     if list_words[left] not in vowels:
        #         left += 1
        #     elif list_words[left] in vowels and list_words[right] in vowels:
        #         list_words[left], list_words[right] = list_words[right], list_words[left]
        #         left += 1
        #         right -= 1
        
        # return "".join(list_words)
        s = list(s)
        vowels = 'aeiouAEIOU'
        l, r = 0, len(s) - 1

        while (l < r):
            while (l < r and s[l] not in vowels):
                l += 1
            while (r > l and s[r] not in vowels):
                r -= 1
            s [l], s[r] = s[r], s[l]

            l +=1
            r -=1
            
        return "".join(s)