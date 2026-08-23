class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # check frequency of every character in s1 for substrings in s2
        # sliding window should be the length of s1

        left = 0
        counterS1 = Counter(s1)
        counterS2 = Counter()

        for right in range(len(s2)):
            counterS2[s2[right]] += 1

            if right - left + 1 > len(s1):
                counterS2[s2[left]] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                if counterS1 == counterS2:
                    return True
        return False


