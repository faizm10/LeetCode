"""
p08. 3Sum (Medium)
Topic: Two Pointers / Sorting

Given an integer array nums, return all unique triplets [a, b, c] such
that a + b + c == 0. The solution set must not contain duplicate triplets.
Order of triplets, and order within a triplet, does not matter.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res


def _normalize(triplets):
    return sorted(sorted(t) for t in triplets)


if __name__ == "__main__":
    assert _normalize(three_sum([-1, 0, 1, 2, -1, -4])) == _normalize([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed!")
