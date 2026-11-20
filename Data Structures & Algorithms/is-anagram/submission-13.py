class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create two maps and compare them, if they are the exact same return True

        if len(s) != len(t):
            return False

        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for char in s:
            sMap[char] += 1
        
        for char in t:
            tMap[char] += 1


        return tMap == sMap