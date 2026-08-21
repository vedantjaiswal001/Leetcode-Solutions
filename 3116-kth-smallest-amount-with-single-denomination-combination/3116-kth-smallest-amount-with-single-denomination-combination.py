from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins.sort()
        useful = []

        for c in coins:
            if all(c % x != 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)
        subs = []

        for mask in range(1, 1 << n):
            l = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    l = (l * coins[i]) // gcd(l, coins[i])

            subs.append((l, bits))

        def count(x):
            ans = 0
            for l, bits in subs:
                if l <= x:
                    if bits & 1:
                        ans += x // l
                    else:
                        ans -= x // l
            return ans

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo