class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        g = []
        d = set()
        f= set()
        for i in nums1:
            if i not in nums2:
                d.add(i)
        g.append(d)
        for j in nums2:
            if j not in nums1:
                f.add(j)
        g.append(f)
        return g