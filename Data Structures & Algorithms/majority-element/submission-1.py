class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums)/2
        
        hashMap = {}

        for i, num in enumerate(nums):
            hashMap[num] = hashMap.get(num,0) + 1
            if hashMap[num] > half:
                return num