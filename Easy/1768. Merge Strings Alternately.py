class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):  # Use len(word1) to get the length
                merge += word1[i] + word2[i]
        else:
            max_length = min(len(word1), len(word2))
            for i in range(max_length):
                # word 1 is 5
                # word 2 is 7
                # last 2 chars in word 2 will be appended to the end of the string
                merge += word1[i] + word2[i]
            merge += word1[max_length:] + word2[max_length:]

        return merge
