class Solution:
    def firstDuplicate(nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        return -1