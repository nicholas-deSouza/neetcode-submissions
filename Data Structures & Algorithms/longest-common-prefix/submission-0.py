class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]

        prefix = ""
        
        for i in range(len(first_string)):
            for word in strs:
                if i == len(word) or word[i] != first_string[i]:
                    return prefix

            prefix += strs[0][i]
        return prefix
