class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(map(int, sorted(str(num), reverse = True)))
        answer = 0
        position = 0
        for i in range(len(nums)):
            answer += nums[i] * 10 ** position  
            if i%2==1:
                position += 1
        return answer