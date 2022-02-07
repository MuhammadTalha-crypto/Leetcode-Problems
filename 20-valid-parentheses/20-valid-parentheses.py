class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return true
        
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' and (len(stack) == 0 or stack[-1] !='('):
                return False
            elif c == '}' and (len(stack) == 0 or stack[-1] !='{'):
                return False
            elif c == ']' and (len(stack) == 0 or stack[-1] !='['):
                return False
            else:
                stack.pop()
        if len(stack) > 0:
            return False
        
        return True
            
            
            
            
        
        
            