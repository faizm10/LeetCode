class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        numbers = set(nums)

        for num in numbers:
            if num - 1 not in numbers:
                length = 1
                current = num

                while num+1 in numbers:
                    current = num+1
                    current += 1
                    length += 1

                longest = max(longest,length)
        return longest