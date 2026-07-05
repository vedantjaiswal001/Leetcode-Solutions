class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        arr=[]
        b=-1

        for i in nums:
            temp=i
            big=0
            small=9

            while temp>0:
                digit = temp % 10
                big=max(big,digit)
                small=min(small,digit)
                temp=temp//10

            dif=big-small
            arr.append((i,dif))
            b=max(b,dif)

        ans=0
        for i, dif in arr:
            if dif==b:
                ans+=i
        return ans©leetcode