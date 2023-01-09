class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        number = 0
        
        for i in range(len(nums)):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                number += 1
        
        return number
        
        