class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len) # 
        for item in strs: # When item = "flight"
            while len(short) > 0:
                if item.startswith(short):# during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                    break
                else:
                    short = short[:-1]# during loop 1 short = flo, during loop 2 short = fl
        return short

        