from collections import Counter

class Solution:

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        a = Counter(s)
        b = [x for x in a if a[x] % 2]

        if len(b) > 1:
            return ""

        c = b[0] if b else ""
        d = []

        for x in sorted(a):
            d += [x] * (a[x] // 2)

        def e(f):
            return f + c + f[::-1]

        f = Counter(d)
        g = ""
        h = ""

        for i in range(len(d)):
            j = ""

            for k in sorted(f):
                if k > target[i] and f[k] > 0:
                    j = k
                    break

            if j:
                l = f.copy()
                l[j] -= 1

                m = g + j

                for k in sorted(l):
                    m += k * l[k]

                h = e(m)

            if f[target[i]] == 0:
                break

            f[target[i]] -= 1
            g += target[i]

        else:
            i = e(g)

            if i > target:
                return i

        return h