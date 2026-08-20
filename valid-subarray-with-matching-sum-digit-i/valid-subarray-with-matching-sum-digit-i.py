class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n=len(nums)
        a=0
        vedu=(nums,x)
        for i in range (n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if s%10!=x:
                    continue
                t=s
                while t>=10:
                    t=t//10
                if t==x:
                    a+=1
        return a©leetcode
