class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r1=set()
        c1=set()
        c=len(matrix[0])
        r=len(matrix)
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    r1.add(i)
                    c1.add(j)
        for i in r1:
            for j in range(c):
                matrix[i][j]=0
        for j in c1:
            for i in range(r):
                matrix[i][j]=0
        