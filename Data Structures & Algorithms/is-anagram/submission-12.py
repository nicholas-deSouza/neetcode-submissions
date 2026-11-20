class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create two maps and compare them, if they are the exact same return True


        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for char in s:
            sMap[char] += 1
        
        for char in t:
            tMap[char] += 1


        if sMap == tMap:
            return True
        else:
            return False