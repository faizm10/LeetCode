class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) # we calc the length of the list
        i,j,k = 0,1,n-1
        while i<j<k:
            total = nums[i] + nums[j]+ nums[k]
            #we want to check if there all equal to 0
            if (total == 0):
                res.append([nums[i],nums[j],nums[k]])
            elif total > 0:
                k-=1
            elif total < 0:
                j+=1
            i+=1
        return res