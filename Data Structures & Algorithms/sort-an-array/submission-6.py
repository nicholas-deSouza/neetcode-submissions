class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        indexInNums = 0
        minVal = min(nums)
        maxVal = max(nums)
        counter = Counter(nums)

        for val in range(minVal, maxVal + 1):
            while counter[val] > 0:
                nums[indexInNums] = val
                counter[val] -= 1
                indexInNums += 1
        return nums
            