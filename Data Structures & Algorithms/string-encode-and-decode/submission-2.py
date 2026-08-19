class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for string in strs:
            length = len(string)
            res.append(str(length) + "#" + string)
        

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []

        right = 0
        
        while right < len(s):
            left = right
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = length + left
            res.append(s[left:right])
            left = right 
        return res 
    
        # 5#Hello5#World