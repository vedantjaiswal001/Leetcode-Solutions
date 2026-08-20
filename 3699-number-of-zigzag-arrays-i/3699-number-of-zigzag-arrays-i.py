class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        if n == 2:
            return m * (m - 1) % MOD

        for _ in range(3, n + 1):
            p = [0] * (m + 1)
            s = [0] * (m + 1)

            for i in range(m):
                p[i + 1] = (p[i] + down[i]) % MOD

            for i in range(m - 1, -1, -1):
                s[i] = (s[i + 1] + up[i]) % MOD

            nu = [0] * m
            nd = [0] * m

            for i in range(m):
                nu[i] = p[i]
                nd[i] = s[i + 1]

            up = nu
            down = nd

        ans = (sum(up) + sum(down)) % MOD
        return ans
