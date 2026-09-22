class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        prod = [1] * (4 * n)
        cnt = [[0] * k for _ in range(4 * n)]

        def pull(node):
            left = node * 2
            right = left + 1

            prod[node] = (prod[left] * prod[right]) % k

            for r in range(k):
                cnt[node][r] = cnt[left][r]

            for r in range(k):
                new_r = (prod[left] * r) % k
                cnt[node][new_r] += cnt[right][r]

        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                prod[node] = val
                cnt[node][val] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node)

        def update(node, l, r, idx, value):
            if l == r:
                value %= k
                prod[node] = value
                cnt[node] = [0] * k
                cnt[node][value] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            pull(node)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            left_prod, left_cnt = left
            right_prod, right_cnt = right

            total_prod = (left_prod * right_prod) % k
            total_cnt = left_cnt[:]

            for r in range(k):
                new_r = (left_prod * r) % k
                total_cnt[new_r] += right_cnt[r]

            return total_prod, total_cnt

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None

            if ql <= l and r <= qr:
                return prod[node], cnt[node][:]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, prefix_count = query(1, 0, n - 1, start, n - 1)

            ans.append(prefix_count[x])

        return ans