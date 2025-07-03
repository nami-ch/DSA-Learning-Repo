#-- soln 1: O(n2 +nlogn) time and space - o(1)
def threesum(nums):
    n = len(nums)
    res = set()
    nums.sort()

    for i in range(n):
        target = -nums[i]
        left, right = 0, n - 1

        while left < right:
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue

            s = nums[left] + nums[right]

            if s == target:
                triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                res.add(triplet)
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1

    return [list(t) for t in res]
