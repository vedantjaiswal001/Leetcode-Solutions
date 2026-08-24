class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        dp = prefix[n]
        for i in range(n - 2, 0, -1):
            dp = max(prefix[i + 1] - dp, dp)
        return dp