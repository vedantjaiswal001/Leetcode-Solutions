# Maximum Building Height

Build n buildings in a line with height 0 at building 1. Heights must be non-negative integers, and adjacent buildings can differ by at most 1. Given maximum height restrictions for certain buildings, determine the highest possible height any building can achieve while satisfying all constraints.

## Approach

### Step 1: Add Mandatory Restrictions

Building `1` must have height `0`, so we add the restriction `[1, 0]`. We also add `[n, n-1]` because starting from height `0`, the maximum possible height at building `n` cannot exceed `n-1` due to the adjacent height difference constraint.

### Step 2: Sort Restrictions

Sort all restrictions by building index so that they can be processed from left to right.

### Step 3: Left-to-Right Relaxation

For every restriction, ensure that it can be reached from the previous restricted building. If the current maximum height exceeds the previous height plus the distance between the two buildings, reduce it accordingly.

`height[i] = min(height[i], height[i-1] + distance)`

### Step 4: Right-to-Left Relaxation

Process the restrictions in reverse order to ensure each restriction can also be reached from the right side.

`height[i] = min(height[i], height[i+1] + distance)`

After these two passes, all restrictions become mutually consistent.

### Step 5: Compute Maximum Possible Peak

For every pair of consecutive restricted buildings `(x1, h1)` and `(x2, h2)`, the tallest possible building between them is obtained by increasing the height as much as possible and then decreasing to satisfy the second restriction.

The maximum achievable height in that interval is:

`(h1 + h2 + (x2 - x1)) // 2`

Compute this value for every adjacent pair and return the maximum.

### Complexity Analysis

* Time Complexity: `O(m log m)` due to sorting, where `m` is the number of restrictions.
* Space Complexity: `O(1)` extra space (excluding the input array).

This approach efficiently handles the large constraint `n ≤ 10^9` by processing only the restricted buildings instead of all buildings.
