class Solution:
    def isValid(self, s: str) -> bool:
        # s =""
        if not s or len(s) == 0:
            return True
        # (  )       ( [ { } ] )    [   )   ) { }
        stack = [] #O(n)
        for c in s:    #O(n)
            if c =='('or c =='{' or c =='[':
                stack.append(c)
            elif c ==')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            elif c =='}' and (len(stack) == 0 or stack[-1] != '{'):
                return False
            elif c ==']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            else:
                stack.pop()
                
        if len(stack) > 0:
            return False
        
        return True
            