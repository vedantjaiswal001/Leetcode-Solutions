class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                curr = stack.pop()
                score = 1 if curr == 0 else 2 * curr
                stack[-1] += score

        return stack[0]
        