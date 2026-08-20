# 1358. Number of Substrings Containing All Three Characters

Sliding Window (Two Pointers): Expand the right pointer while counting a, b, and c. Once the window contains all three characters, every substring ending at or after right is valid, so add n - right to the answer. Shrink the left pointer until the window becomes invalid, then continue. Time: O(n), Space: O(1).

by VEDANT JAISWAL
