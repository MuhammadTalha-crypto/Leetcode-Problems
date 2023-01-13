class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length=len(nums)
        listt=[0]*(length)
        for i in range(2,length):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                listt[i]=1+listt[i-1]
        return sum(listt)
        
            
        