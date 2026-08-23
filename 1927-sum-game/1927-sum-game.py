class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        diff = 0
        q1 = q2 = 0

        for i in range(n):
            if num[i] == '?':
                q1 += 1
            else:
                diff += int(num[i])

        for i in range(n, 2 * n):
            if num[i] == '?':
                q2 += 1
            else:
                diff -= int(num[i])

        if (q1 + q2) % 2 != 0:
            return True

        return diff != 9 * (q2 - q1) // 2