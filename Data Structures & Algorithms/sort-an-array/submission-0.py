class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            # don't have to worry about key errors
            count = defaultdict(int)

            minVal = min(nums)
            maxVal = max(nums)

            for val in nums:
                count[val] += 1

            indexInArray = 0

            # + 1 is necessary since minVal and maxVal are values not indices
            for val in range(minVal, maxVal + 1):
                while count[val] > 0:
                    nums[indexInArray] = val
                    indexInArray += 1
                    count[val] -= 1
    
        counting_sort()
        return nums