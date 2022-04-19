class Solution:
    def myPow(self, x: float, n: int) -> float:
        #1st very simple answer
        # ans = x**n
        # return ans
        if n ==0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n%2==0:
            half = self.myPow(x,n/2)
            return half * half
        else:
            return x * self.myPow(x,n-1)
        