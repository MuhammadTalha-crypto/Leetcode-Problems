class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                new.append(True)
            else:
                new.append(False)
        return new
            
            
            
            # # a = candies[i] + extraCandies
            # for j in range(i+1, len(candies)):
            #     if (candies[i] + extraCandies) > candies[j]:
            #         new.append(True)
            #     else:
            #         new.append(False)
        # return new
        