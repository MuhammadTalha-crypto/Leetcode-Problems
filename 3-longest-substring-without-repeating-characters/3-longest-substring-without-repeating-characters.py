class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        dic = {}
        r = l = 0
        for i in range(len(s)):
            if s[i] in dic and l <= dic[s[i]]:
                l = dic[s[i]] + 1
            else:
                r = max(r, i-l+1)
            dic[s[i]] = i
        return r
        