class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = nums1 + nums2
        out.sort()
        if len(out) % 2 != 0:
            print("odd")
            mid = (len(out) - 1) // 2
            print("mid: ", mid)
            return out[mid]
        else:
            print("even")
            n = len(out)
            middle_index_1 = n // 2 - 1 
            middle_index_2 = n // 2    
            median = (out[middle_index_1] + out[middle_index_2] ) / 2 
            return median
            