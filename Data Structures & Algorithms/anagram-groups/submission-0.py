class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for string in strs:
            sorted_string = sorted(string)
            joined = "".join(sorted_string)
            if joined not in hash_map:
                hash_map[joined] = []
            hash_map[joined].append(string)
        return list(hash_map.values())
