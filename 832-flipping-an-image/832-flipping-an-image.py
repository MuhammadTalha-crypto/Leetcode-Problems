class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        c = []
        for i in image:
            i.reverse()
            b = []
            for n in i:
                if n == 1:
                    b.append(0)
                elif n==0:
                    b.append(1)
            c.append(b)
        return c