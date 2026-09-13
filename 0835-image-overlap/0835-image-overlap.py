class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for x in range(-n + 1, n):
            for y in range(-n + 1, n):
                c = 0
                for i in range(n):
                    for j in range(n):
                        if 0 <= i + x < n and 0 <= j + y < n:
                            c += img1[i][j] & img2[i + x][j + y]
                ans = max(ans, c)

        return ans