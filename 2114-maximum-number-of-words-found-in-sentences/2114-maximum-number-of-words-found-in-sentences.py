class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ls = []
        c = 0
        for sentence in sentences:
            d = sentence.split()
            count = len(d)
            ls.append(count)
        for i in range(len(ls)):
            if ls[i] > c:
                c = ls[i]
        return c
        