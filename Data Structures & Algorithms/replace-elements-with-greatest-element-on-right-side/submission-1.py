class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # two pointer approach, modify array in place

        max_so_far = -1
        for i in range(len(arr) - 1 , -1 , -1):
            current_val = arr[i]
            arr[i] = max_so_far
            max_so_far = max(current_val, max_so_far)
        return arr

