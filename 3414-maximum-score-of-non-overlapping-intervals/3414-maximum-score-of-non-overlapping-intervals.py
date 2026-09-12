class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = sorted((x[0], x[1], x[2], i) for i, x in enumerate(intervals))
        s = [x[0] for x in a]

        from bisect import bisect_right
        from functools import lru_cache

        @lru_cache(None)
        def f(i, k):
            if i == n or k == 0:
                return 0, ()

            x, y = f(i + 1, k)
            j = bisect_right(s, a[i][1])
            z, q = f(j, k - 1)
            z += a[i][2]
            q = tuple(sorted((a[i][3],) + q))

            if z > x or z == x and q < y:
                return z, q
            return x, y

        return list(f(0, 4)[1])