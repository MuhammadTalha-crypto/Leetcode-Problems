class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        para = 0
        for i in s:
            if i == "(":
                count +=1
            if para < count:
                para = count
            elif i == ")":
                count -=1
                
        return para
        