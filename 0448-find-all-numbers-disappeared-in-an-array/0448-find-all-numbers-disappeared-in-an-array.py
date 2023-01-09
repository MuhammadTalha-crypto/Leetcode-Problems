class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        #Solution 1
        return set(range(1, len(nums) + 1)) - set(nums)
    

                
        