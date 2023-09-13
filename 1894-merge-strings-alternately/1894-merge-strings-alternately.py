class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        if len(word1) > len(word2):
            max_len = len(word1)
        else:
            max_len = len(word2)
        print(max_len)
        iterative_over = min(len(word1), len(word2))
        if iterative_over == 0:
            for i in range(len(word1)):
                merged += word1[i]
                merged += word2[i]    
        else:
            for i in range(iterative_over):
                merged += word1[i]
                merged += word2[i]

        if len(word1) > len(word2):
            merged += word1[iterative_over:]
        elif len(word2) > len(word1):
            merged += word2[iterative_over:]
        return merged
