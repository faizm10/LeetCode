class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [ [0]*(i+1) for i in range(numRows) ]

        for i in range(numRows): 
            triangle[i][0] = 1 # left side of each rows are 1
            triangle[i][i] = 1 # right side of each rows are 1
            
        for i in range(2,numRows):
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        return triangle