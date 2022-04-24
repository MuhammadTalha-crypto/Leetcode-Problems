class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        # k = 0
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
            i +=1
            # k +=1
        return ans
        
        