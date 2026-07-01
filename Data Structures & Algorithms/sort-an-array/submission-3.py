class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for val in nums:
            count[val] += 1

        minVal = min(nums)
        maxVal = max(nums)

        indexInArray = 0

        for val in range(minVal, maxVal + 1):
            while count[val] > 0:
                nums[indexInArray] = val
                count[val] -= 1
                indexInArray += 1
        return nums