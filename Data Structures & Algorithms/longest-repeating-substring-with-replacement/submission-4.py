class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k is the amount we can replace
        # need to keep track of the max in the window

        left = 0
        counter = Counter()
        max_freq = 0
        longest = 1

        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])
            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

                

