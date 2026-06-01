class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freqMap1 = {}
        freqMap2 = {}

        for char in s:
            freqMap1[char] = freqMap1.get(char, 0) + 1

        for char in t:
            freqMap2[char] = freqMap2.get(char, 0) + 1

        if freqMap1 == freqMap2:
            return True
        return False