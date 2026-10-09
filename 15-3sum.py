class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # use two pointers to make sure numbers are unique and it adds up to 0

        result = []
        nums.sort()
        for i in range(len(nums)):
            
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]: continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 :
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
            
        return result
            