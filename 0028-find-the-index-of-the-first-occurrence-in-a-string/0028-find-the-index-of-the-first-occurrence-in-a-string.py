class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge cases
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1

        # Build LPS (Longest Prefix-Suffix) for needle — KMP preprocessing
        lps = [0] * len(needle)
        j = 0  # length of current matched prefix in needle
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j

        # KMP search
        i = j = 0  # i over haystack, j over needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  # match start index
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
