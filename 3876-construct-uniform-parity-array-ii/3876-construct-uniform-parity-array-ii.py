class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        e = False
        o = False

        for x in nums1:
            if x % 2 == 0:
                e = True
            else:
                o = True

        if not e or not o:
            return True

        return min(nums1) % 2 == 1
        