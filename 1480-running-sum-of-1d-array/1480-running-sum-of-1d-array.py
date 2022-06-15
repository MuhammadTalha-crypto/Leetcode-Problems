class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        for i in range(len(nums)):
            k +=nums[i]
            ans.append(k)
        return ans