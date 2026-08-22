class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=str(n)
        sumi=0
        pro=1
        y=str(n)
        for i in x:
            a=int(i)
            sumi=sumi+a
            pro=pro*a
        sumi=sumi+pro
        if n%sumi==0:
            return True
        else:
            return False
        