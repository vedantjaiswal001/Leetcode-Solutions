class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=str(n)
        sumi=0
        pro=1
        y=str(n)
        for i in x:
            sumi=sumi+int(i)
            pro=pro*int(i)
        sumi=sumi+pro
        if n%sumi==0:
            return True
        else:
            return False
        