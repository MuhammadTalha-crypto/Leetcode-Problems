class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        for n in nums:
            if n not in visited:
                visited[n] = 1
            else:
                visited[n] += 1
        for n in nums:
            if visited[n] ==1:
                return n
        