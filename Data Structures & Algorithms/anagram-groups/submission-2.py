class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort all the strings and add them to dict

        # sorted string: string 

        # default value is a list, no explicit check will need to be made

        hash_map = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            hash_map[sorted_string].append(string)
        return list(hash_map.values())


        