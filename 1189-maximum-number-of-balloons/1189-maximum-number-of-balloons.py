class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = {}
        
        for ch in text:
            c[ch] = c.get(ch, 0) + 1
        
        return min(
            c.get('b', 0),
            c.get('a', 0),
            c.get('l', 0) // 2,
            c.get('o', 0) // 2,
            c.get('n', 0)
        )
        
