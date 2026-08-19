class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = not (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)))
            mid = not (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)))
            right = not (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)))

            if left and right:
                ans += 2
            elif left or mid or right:
                ans += 1

        return ans