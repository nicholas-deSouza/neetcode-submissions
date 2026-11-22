class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineDict = Counter(magazine)

        for char in ransomNote:
            if magazineDict[char] < 1:
                return False
            else:
                magazineDict[char] -= 1
        return True


