class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result,seen,index = "",[],0
        for i in range(len(s)):
            if s[i] == "(":
                seen.append(s[i])
            elif s[i] == ")":
                seen.pop()
                if not seen:
                    result += s[index+1:i]
                    index = i+1
        return result
            
            
        