class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        max_wealth = 0
        for i in accounts:
            count = sum(i)
            max_wealth = max(max_wealth, count)
        return max_wealth
                
                
        