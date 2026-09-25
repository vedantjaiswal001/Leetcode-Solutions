class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        i = 0

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse_expr():
            nonlocal i

            res = parse_term()

            while i < n and expression[i] == ',':
                i += 1
                res |= parse_term()

            return res

        def parse_term():
            nonlocal i

            res = {""}

            while i < n and expression[i] not in "},":
                res = product(res, parse_factor())

            return res

        def parse_factor():
            nonlocal i

            if expression[i].isalpha():
                ch = expression[i]
                i += 1
                return {ch}

            i += 1
            res = parse_expr()
            i += 1
            return res

        return sorted(parse_expr())
        