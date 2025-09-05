# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#Input: nums = [1,2,2,3,3,3], k = 2
#Output: [2,3]

def topKFrequent(nums, k):  
    unique_numbers = set()
    list = []
    for num in nums:
        if num not in unique_numbers:  # Check if the number is already in the set
            unique_numbers.add(num)    # Add to the set to mark it as seen
            list.append(num)        # Add to the list
    return list