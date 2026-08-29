class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        a = sorted((x, i) 
        for i, x in enumerate(nums))
        n = len(nums)
        i = 0

        while i < n:
            j = i

            while j + 1 < n and a[j + 1][0] - a[j][0] <= limit:
                j += 1

            b = sorted(a[k][1] for k in range(i, j + 1))

            for k, x in enumerate(b):
                nums[x] = a[i + k][0]

            i = j + 1

        return nums