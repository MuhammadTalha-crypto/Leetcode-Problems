class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor1 = 0
        for i in nums:
            xor1 ^= i
        
        lowestBit = xor1 & (-xor1)
        res = [0]*2
        print('res', res)
        for i in range(n):
            if(lowestBit & nums[i] == 0):
                print('inums[i]', nums[i])
                res[0] ^= nums[i]
                print(res[0])
            else:
                print('enums[i]', nums[i])
                res[1] ^= nums[i]
                print(res[1])
        
        return res
                
                
                
        