class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        s = 0

        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)

        ans = 0

        for i in range(1, n + 1):
            for j in range(i):
                if pref[j] < pref[i]:
                    ans += 1

        return ans
        
