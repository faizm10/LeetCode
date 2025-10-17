class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        low = 100
        while left<=right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            current = nums[mid]
            if low > nums[mid]:
                low = nums[mid]
        return low
            

                