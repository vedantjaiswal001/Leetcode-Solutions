
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        
        ans = 0
        for i in range(n):
            square = nums[i] * nums[i]
            if i < n // 2:
                ans -= square
            else:
                ans += square
                
        return ans
