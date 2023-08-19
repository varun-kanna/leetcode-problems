class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash1 = {}
        hash2 = {}

        for i in s:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1

        for z in t:
            if z not in hash2:
                hash2[z] = 1
            else:
                hash2[z] += 1
        
        return hash1 == hash2
