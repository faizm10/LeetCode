class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) # we calc the length of the list
        for i,k in enumerate(nums):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l,r = i + 1, n - 1
            while l < r:
                total = k + nums[l]+ nums[r]
                #we want to check if there all equal to 0
                if (total == 0):
                    res.append([k,nums[l],nums[r]])
                    l+=1
                    while nums == nums[i-1] and l<r:
                        l+=1
                elif total > 0:
                    r-=1
                elif total < 0:
                    l+=1
        return res
        