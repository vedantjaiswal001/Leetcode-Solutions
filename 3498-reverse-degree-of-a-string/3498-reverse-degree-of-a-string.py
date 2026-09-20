class Solution:
    def reverseDegree(self, s: str) -> int:
        sumi=0
        for i in range(0,len(s)):
            sumi=sumi+(26-((ord(s[i]))-97))*(i+1)
        return sumi

        