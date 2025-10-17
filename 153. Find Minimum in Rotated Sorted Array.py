class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        min = 100
        while i<j:
            mid = (nums[i]+nums[j]) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid