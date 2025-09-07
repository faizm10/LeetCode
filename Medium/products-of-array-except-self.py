class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = 1
        left = 1
        n = len(nums)
        result = [0] * n #init the entire array

        for i in range(n):
            prod = 1
            for g in range(n):
                if i == g:
                    continue
                prod *= nums[g]
            result[i] = prod 
        return result
            
            
        return result