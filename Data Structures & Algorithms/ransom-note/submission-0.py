class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # a: 2
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        
        for letter in ransomCounter:
            if magazineCounter[letter] < ransomCounter[letter]:
                return False
        return True



