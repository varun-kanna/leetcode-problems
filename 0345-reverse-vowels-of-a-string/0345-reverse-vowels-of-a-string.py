class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        list_words = list(s)

        left, right = 0, len(list_words) - 1

        while left <= right:
            if list_words[right] not in vowels:
                right -= 1
            if list_words[left] not in vowels:
                left += 1
            elif list_words[left] in vowels and list_words[right] in vowels:
                list_words[left], list_words[right] = list_words[right], list_words[left]
                left += 1
                right -= 1
        
        return "".join(list_words)
        