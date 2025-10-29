class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        ans = 0
        for i, t in enumerate(tickets):
            if i <= k:
                ans += min(t, x)
            else:
                ans += min(t, x - 1)
        return ans
