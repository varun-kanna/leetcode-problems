class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j = 0,0
        merged = []

        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        if len(word1) > len(word2):
            merged.append(word1[i:])
        elif len(word2) > len(word1):
            merged.append(word2[j:])
        return "".join(merged)