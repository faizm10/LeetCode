class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        out = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                out.append(nums1[i]); i += 1
            else:
                out.append(nums2[j]); j += 1
        out.extend(nums1[i:]); 
        out.extend(nums2[j:])
        if len(out) % 2 != 0:
            end = len(out)-1
            mid = out[0] - out[end]
            return out[mid]
        else:
            n = len(out)
            middle_index_1 = n // 2 - 1 
            middle_index_2 = n // 2    
            median = (out[middle_index_1] + out[middle_index_2] ) / 2 
            return median
            