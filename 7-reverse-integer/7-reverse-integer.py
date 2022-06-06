class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1
        if x< 0:
            sign = -1
            x = x * -1
        while x>0:
            remainder = x % 10
            sum = sum* 10 +remainder
            x = x//10
        if not -2147483648<sum<2147483647:
            return 0
        return sign*sum
        
        
            
            
            