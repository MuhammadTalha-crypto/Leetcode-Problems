class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        i, j = 0, len(s) - 1
        #len(hello) = 5 - 1 = 4
        while i < j:
            if lst[i] not in "aeiouAEIOU":
                i += 1 # i = i + 1
            elif lst[j] not in "aeiouAEIOU":
                j -=1  # j = j-1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i+=1
                j-=1
        return "".join(lst)
    
    
    
    # l     e     e     t     c     o     d     e
        