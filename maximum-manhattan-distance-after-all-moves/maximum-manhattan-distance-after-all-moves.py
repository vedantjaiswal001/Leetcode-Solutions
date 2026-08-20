class Solution:
    def maxDistance(self, moves: str) -> int:
        x=0
        y=0
        k=0
        for c in moves:
            if c =="L":
                x-=1
            elif c=="R":
                x+=1
            elif c=="U":
                y+=1
            elif c=="D":
                y-=1
            else:
                k+=1

        return abs(x)+abs(y)+k
