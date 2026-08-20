class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        st = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            ans = max(ans, r - l + 1)

        return ans
