class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # iterate backwards 

        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, val)
        return arr