class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = candies[0]
        for i in range(len(candies)):
            if candies[i]>=max:
                max = candies[i]
        result = [True] * len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max:
                result[i] = True
            else:
                result[i] = False
        return result