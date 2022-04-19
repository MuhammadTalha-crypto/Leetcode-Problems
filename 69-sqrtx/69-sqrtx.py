class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while (left <= right):
            mid = (left + right)//2
            midsqr = mid*mid
            if midsqr ==x:
                return mid
            elif midsqr <x:
                left = mid+1
                ans = mid
            else:
                right = mid-1
        return ans
        
        