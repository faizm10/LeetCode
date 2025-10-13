class Solution:
    def topKFrequent(self, nums, k):
        cnt = Counter(nums) 
        a = cnt.most_common(k)
        top_k_elements = [x for x, _ in a]
        return top_k_elements