# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(r):
            nonlocal ans

            if not r:
                return 0, 0

            s1, n1 = dfs(r.left)
            s2, n2 = dfs(r.right)

            s = s1 + s2 + r.val
            n = n1 + n2 + 1

            if r.val == s // n:
                ans += 1

            return s, n

        dfs(root)
        return ans
        