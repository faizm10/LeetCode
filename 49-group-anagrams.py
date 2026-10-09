class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = {}

        for i in strs:
            word = "".join(sorted(i))
            if word not in grouped:
                grouped[word] = []
            grouped[word].append(i)

        return list(grouped.values())