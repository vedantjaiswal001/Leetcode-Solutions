class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines = sum // 9
        rem = sum % 9

        result = "9" * nines

        if rem > 0:
            result += str(rem)

        result += "0" * (num - len(result))

        return result