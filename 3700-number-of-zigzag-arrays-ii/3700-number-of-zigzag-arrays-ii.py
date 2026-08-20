class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1
        s = 2 * m

        t = [[0] * s for _ in range(s)]

        for i in range(m):
            for j in range(i):
                t[i][m + j] = 1

        for i in range(m):
            for j in range(i + 1, m):
                t[m + i][j] = 1

        v = [0] * s

        for i in range(m):
            v[i] = i
            v[m + i] = m - 1 - i

        def mm(a, b):
            c = [[0] * s for _ in range(s)]

            for i in range(s):
                for k in range(s):
                    if a[i][k] == 0:
                        continue

                    x = a[i][k]

                    for j in range(s):
                        if b[k][j]:
                            c[i][j] = (c[i][j] + x * b[k][j]) % MOD

            return c

        def mv(a, v):
            r = [0] * s

            for i in range(s):
                cur = 0

                for j in range(s):
                    if a[i][j]:
                        cur = (cur + a[i][j] * v[j]) % MOD

                r[i] = cur

            return r

        p = n - 2

        while p:
            if p & 1:
                v = mv(t, v)

            t = mm(t, t)
            p >>= 1

        return sum(v) % MOD
