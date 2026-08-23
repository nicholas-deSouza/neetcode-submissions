class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineCounter = Counter(magazine)

        for letter in ransomNote:
            if magazineCounter[letter] > 0:
                magazineCounter[letter] -= 1
            else:
                return False
        return True