class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            answer.append(sum1)
        return answer