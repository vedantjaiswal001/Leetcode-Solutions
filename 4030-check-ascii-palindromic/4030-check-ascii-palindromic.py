class Solution:
    def isPalindromic(self, s: str) -> bool:
        b = ""
        for c in s:
            b += format(ord(c), '08b')
        
        return b == b[::-1]