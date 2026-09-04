class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        a = [0] * n

        a[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            a[i] = min(nums[i], a[i + 1])

        m = nums[0]

        for i in range(n):
            m = max(m, nums[i])

            if m - a[i] <= k:
                return i

        return -1