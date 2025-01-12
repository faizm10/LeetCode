class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # creates list if empty, otherwise add to the list
        for s in strs:
            sortedS = ''.join(sorted(s)) # breaks down each letter and then sorts it
            res[sortedS].append(s)
        return list(res.values())