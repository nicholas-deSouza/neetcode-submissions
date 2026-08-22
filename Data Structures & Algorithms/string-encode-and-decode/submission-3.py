class Solution:

    def encode(self, strs: List[str]) -> str:
        # use a delimiter 

        res = []

        for string in strs:
            length = str(len(string))
            res.append(length + "#" + string)
        
        return "".join(res) 

    def decode(self, s: str) -> List[str]:
        
        res = []
        right = 0
        # 5#Hello5#World
        while right < len(s) - 1:
            left = right
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            word = s[left:right]
            res.append(word)
            left = right
        return res