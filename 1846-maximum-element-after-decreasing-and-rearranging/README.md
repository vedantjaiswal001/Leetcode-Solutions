# 1846. Maximum Element After Decreasing and Rearranging

Sort the array. Set the first element to 1. Traverse from left to right, updating each element as min(arr[i], arr[i-1] + 1). This keeps adjacent differences ≤ 1 while maximizing every value greedily. The last element is the maximum possible answer. Time: O(n log n), Space: O(1) (excluding sorting).
