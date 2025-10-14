class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we want to find the two indices of the two number that adds up to the target
        i = 0
        j = len(numbers) - 1
        total = numbers[i] + numbers[j]
        index = []
        while i<j:
            print("i", i)
            print("j", j)
            print("total: ", total)
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1,j+1]
            elif target < total:
                j-=1
            elif target > total:
                i+=1
        return [i,j]