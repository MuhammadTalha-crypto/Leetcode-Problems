class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        total = 0
        for i in jewels:
            s.add(i)
        for n in stones:
            if n in s:
                total +=1
        return total
        