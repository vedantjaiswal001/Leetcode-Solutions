class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        r = 1
        if 1 in c:
            r = c[1] - (1 - c[1] % 2)
        for x in c:
            if x == 1:
                continue
            t = 0
            v = x
            while v in c and c[v] >= 2:
                t += 2
                v = v * v
            if v in c:
                t += 1
            else:
                t -= 1
            r = max(r, t)
        return r
