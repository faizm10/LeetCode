# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#Input: nums = [1,2,2,3,3,3], k = 2
#Output: [2,3]
class Solution:
    def topKFrequent(self, nums, k):
        
        freq = Counter(nums) # init the freq counter 
        buckets = [[] for _ in range(len(nums) + 1)] # create the buckets
        for val, c in freq.items():
            buckets[c].append(val) # fill the buckets
        res = []
        for i in range(len(buckets) - 1, 0, -1): # iterate the buckets in reverse order
            for v in buckets[i]:
                res.append(v)
                if len(res) == k:
                    return res