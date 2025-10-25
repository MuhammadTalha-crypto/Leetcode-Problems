class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True   # we found a duplicate
            seen.add(x)
        return False           # no duplicates at all`
        