class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in range(len(address)):
            if address[i] == ".":
                ans+="[.]"
            elif address[i] !=".":
                ans+=address[i]
        return ans
    
        