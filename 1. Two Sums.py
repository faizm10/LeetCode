class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to find two numbers that add up to the target
        #init the 1st and 2nd indices
        
        #run through the loop now
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]    