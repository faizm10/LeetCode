class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print(sorted(set(nums)))
        arr = sorted(set(nums))
        count = 1
        if nums == []:
            return 0
        for i,x in enumerate(arr):
            if (i < len(arr)-1 and (arr[i+1]-arr[i] == 1)):
                count += 1   # increment
            #i is index
            # x is the value of the infex
        return count

        # answer key:
