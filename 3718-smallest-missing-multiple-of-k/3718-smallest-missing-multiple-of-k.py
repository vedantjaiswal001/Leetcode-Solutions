class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        dic={}
        x=k
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        while True:
            if x in dic:
                x=x+k
                continue
            else:
                return x


        