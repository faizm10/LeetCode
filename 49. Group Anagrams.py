class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to find anagrams for all of em, group the anagrams, etc
        d = defaultdict(list)
        for x in strs:
            key = "".join(sorted(x))
            #print(key)
            d[key].append(x)
            
        return list(d.values())