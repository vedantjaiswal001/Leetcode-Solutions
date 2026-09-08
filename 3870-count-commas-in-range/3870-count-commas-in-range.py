import math
class Solution:
    def countCommas(self, n: int) -> int:
        x=str(n)
        count=0
        if len(x)<=3:
            return 0
        for i in range(1000,n+1,1):
            b=str(i)
            l=len(b)
            z=l/3
            y=math.ceil(z)
            y=y-1
            count=count+y
        return count


        