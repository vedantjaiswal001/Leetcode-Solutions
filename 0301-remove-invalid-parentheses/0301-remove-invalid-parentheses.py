class Solution:
    def removeInvalidParentheses(self, s: str):
        left = right = 0

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        ans = []

        def dfs(i, l, r, balance, path):
            if balance < 0:
                return

            if i == len(s):
                if l == 0 and r == 0 and balance == 0:
                    ans.append(''.join(path))
                return

            c = s[i]

            if c == '(':
                if l > 0:
                    dfs(i + 1, l - 1, r, balance, path)

                path.append(c)
                dfs(i + 1, l, r, balance + 1, path)
                path.pop()

            elif c == ')':
                if r > 0:
                    dfs(i + 1, l, r - 1, balance, path)

                if balance > 0:
                    path.append(c)
                    dfs(i + 1, l, r, balance - 1, path)
                    path.pop()

            else:
                path.append(c)
                dfs(i + 1, l, r, balance, path)
                path.pop()

        dfs(0, left, right, 0, [])
        return list(set(ans))