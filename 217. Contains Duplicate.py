class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = set() # init the set
        for i in nums: # checking every number in nums (list)
            if i in arr: # if index is in the set, it already exists
                return True 
            arr.add(i) # if not, it is unique so we add it to the set
        return False
