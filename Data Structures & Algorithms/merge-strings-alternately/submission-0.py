class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        word1_ptr = 0
        word2_ptr = 0

        while word1_ptr < len(word1) and word2_ptr < len(word2):
            res += word1[word1_ptr]
            res += word2[word2_ptr]
            word1_ptr += 1
            word2_ptr += 1
        # appending the remaining characters to res 
        res += word1[word1_ptr:]
        res += word2[word2_ptr:]
        return res
