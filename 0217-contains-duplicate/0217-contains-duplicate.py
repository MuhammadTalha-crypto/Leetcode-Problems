class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        val = []
        for i in nums:
            if i in val:
                return True
            val.append(i)
        return False
        