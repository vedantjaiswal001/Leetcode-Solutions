class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        prefix = []
        n = len(s)
        i = 0

        while i < n and freq[ord(target[i]) - ord('a')] > 0:
            prefix.append(target[i])
            freq[ord(target[i]) - ord('a')] -= 1
            i += 1

        for j in range(i, -1, -1):
            if j < i:
                freq[ord(prefix[j]) - ord('a')] += 1

            if j < n:
                for c in range(ord(target[j]) - ord('a') + 1, 26):
                    if freq[c] > 0:
                        ans = ''.join(prefix[:j])
                        ans += chr(c + ord('a'))
                        freq[c] -= 1

                        for k in range(26):
                            ans += chr(k + ord('a')) * freq[k]

                        return ans

        return ""