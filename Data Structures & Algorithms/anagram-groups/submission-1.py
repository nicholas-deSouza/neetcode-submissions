class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for string in strs:
            sortedString = ''.join(sorted(string))
            hash_map[sortedString].append(string)
        return list(hash_map.values())
