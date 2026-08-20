# 2812. Find the Safest Path in a Grid

Compute each cell's distance to the nearest thief using multi-source BFS. Then binary search the maximum possible safeness factor. For each candidate, run BFS allowing movement only through cells whose distance is at least that value. The largest valid value is the answer.
