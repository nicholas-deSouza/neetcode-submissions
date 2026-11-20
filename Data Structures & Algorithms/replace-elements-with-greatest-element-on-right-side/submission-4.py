class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # start from the right and replace with the greatest value

        greatestVal = -1 

        for i in range(len(arr) - 1, - 1 , -1):
            temp = arr[i]
            arr[i] = greatestVal
            greatestVal = max(greatestVal, temp)
        return arr