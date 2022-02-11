class Solution:  #w:0, e:1, r:2, t:3, s:4 ----------
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dict = {}
        for x,y in enumerate(order):
            dict[y] = x
            
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for i in range (min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if dict[word1[i]] > dict[word2[i]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
            
        
#         orderInd = {c : i for i, c in enumerate(order)}
        
#         for i in range(len(words) - 1):
#             w1, w2 = words[i], words[i + 1]
#             for j in range(len(w1)):
#                 if j == len(w2):
#                     return False
#                 if w1[i] != w2[j]:
#                     if orderInd[w2[j]] < orderInd[w1[i]]:
#                         return False
#                     break
#         return True
                    
            
            

                