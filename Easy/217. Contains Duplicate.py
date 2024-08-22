class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to keep track of numbers in nums
        seen = set()
        
        # Loop through each number in the list
        for num in nums:
            # Check if the number is already in the set
            if num in seen:  
                # If the number is in the set, it's a duplicate, so return True
                return True
            
            # If the number is not in the set, add it to the set
            seen.add(num)
        
        # If no duplicates are found after checking all numbers, return False
        return False