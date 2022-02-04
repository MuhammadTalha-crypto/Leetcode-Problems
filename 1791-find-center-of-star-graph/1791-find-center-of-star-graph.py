class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # a = edges[0][0]
        # b = edges[0][1]
        # if edges[1][0] == a or edges[1][1] == a:
        #     return a
        # elif edges[1][0] == b or edges[1][1] == b:
        #     return b
    
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
        
     
            