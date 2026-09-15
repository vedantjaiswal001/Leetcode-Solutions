class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        p = [[False] * n for _ in range(n)]

        for i in range(n):
            p[i][i] = True

        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r] and (r - l == 1 or p[l + 1][r - 1]):
                    p[l][r] = True

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i - k + 1):
                if p[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]