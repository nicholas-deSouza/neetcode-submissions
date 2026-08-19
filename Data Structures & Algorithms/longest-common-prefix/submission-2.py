class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_string = strs[0]

        longest = ''

        for i in range(len(first_string)):
            for word in strs:
                if i == len(word) or first_string[i] != word[i]:
                    return longest
            longest += first_string[i]
        return longest