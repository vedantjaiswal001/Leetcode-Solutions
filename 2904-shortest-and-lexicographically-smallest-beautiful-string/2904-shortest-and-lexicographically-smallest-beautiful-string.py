class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            if s[i] == '1':
                count = 0
                for j in range(i, n):
                    if s[j] == '1':
                        count += 1
                    if count == k:
                        sub = s[i:j+1]
                        if res == "" or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                            res = sub
                        break
        return res