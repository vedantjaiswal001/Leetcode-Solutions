# 3699. Number of ZigZag Arrays I

up[i] = ways ending at value i with last move increasing, down[i] = ways ending at i with last move decreasing. Two consecutive increases/decreases are forbidden, so transitions must alternate direction. Use prefix sums of down and suffix sums of up to compute next states in O(m). Overall O(n·m).
