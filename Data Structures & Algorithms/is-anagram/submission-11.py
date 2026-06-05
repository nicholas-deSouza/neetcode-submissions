class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        if len(s) != len(t):
            return False
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for char in s:
            sMap[char] += 1

        for char in t:
            tMap[char] += 1
        
        return sMap == tMap