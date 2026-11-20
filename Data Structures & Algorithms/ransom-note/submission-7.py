class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        magazineDict = Counter(magazine)

        for char in ransomNote:
            if magazineDict[char] > 0:
                magazineDict[char] -= 1
            else:
                return False
        return True
