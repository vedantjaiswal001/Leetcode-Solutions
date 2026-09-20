class Solution:
    def reverseDegree(self, s: str) -> int:
        sumi=0
        for i in range(0,len(s)):
            x=ord(s[i])
            l=x-97
            indi=26-l
            sumi=sumi+indi*(i+1)
        return sumi

        