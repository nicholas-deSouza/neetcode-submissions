class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # space will always be a constant of 26 so it does not scale with the inputs
        # a hash map will also store at most 26 keys but you need a hash calculation for lookup

        count = [0] * 26

        for letter in magazine:
            idxOfLetter = ord(letter) - ord('a')
            count[idxOfLetter] += 1
        
        for letter in ransomNote:
            idxOfLetter = ord(letter) - ord('a')
            count[idxOfLetter] -= 1
            if count[idxOfLetter] < 0:
                return False
        return True