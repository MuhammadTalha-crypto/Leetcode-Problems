class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # pointer in s
        if not s:
            return True
        for ch in t:
            if ch == s[i]:
                i += 1
                if i == len(s):  # matched all of s
                    return True
        return i == len(s)
