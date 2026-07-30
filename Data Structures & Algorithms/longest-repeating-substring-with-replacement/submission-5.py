class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = Counter()
        maxf = 0
        longest = 0
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            maxf = max(maxf, counter[s[right]])
            if (right - left + 1) - maxf > k:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest