class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        ans = sum(prices)

        for i in range(min(len(prices), len(discounts))):
            ans -= prices[i] * discounts[i] / 100

        return ans