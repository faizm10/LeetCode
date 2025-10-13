class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums) #init the array
        i=1
        k=1
        for i in range(len(nums)): 
            prod = 1
            for k in range(len(nums)):        # i = 0,1,2
                if i != k:
                    print("i",i)
                    print("k",k)
                    prod *= nums[k]
            a[i] = prod
        return a     