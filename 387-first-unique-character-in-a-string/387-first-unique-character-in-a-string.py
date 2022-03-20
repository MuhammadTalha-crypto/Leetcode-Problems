class Solution:
    def firstUniqChar(self, s: str) -> int:
        n ={}
        for i in s:
            if i not in n:
                n[i] = True
            else:
                n[i] = False
    
        for j in range(0,len(s)):
            if n[s[j]]:
                return j
        return -1
            
            
                
        