class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Map = {}
        for i in nums:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i] += 1
                return True
            
                
                
        