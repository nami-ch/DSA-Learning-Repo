# Sliding Window Algorithm Notes

## What I Learned
- Sliding window is a technique for problems involving contiguous sequences — subarrays/substrings.
- It helps optimize brute force solutions that would otherwise be O(n²) or worse.
- There are two types:
  - **Fixed-size window** (when the length of the window is known beforehand)
  - **Variable-size window** (when constraints dynamically define window size)

---

## 📌 Pseudo Code / Sample Implementation

### 🔒 Fixed-size Window

**Goal**: Find maximum sum of a subarray of size `k`

```python
n = len(arr)
if n < k:
    return None

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

return max_sum
```

### 🔒 Variable-size Window

**Goal**: Find the length of the longest substring with at most `k` distinct characters 

```python
from collections import defaultdict

left = 0
total = 0
min_len = float('inf')

for right in range(len(nums)):
  total += nums[right]

  while total >= target:
    min_len = min(min_len, right - left + 1)
    total -= nums[left]
    left += 1

return 0 if min_len == float('inf') else min_len

```
