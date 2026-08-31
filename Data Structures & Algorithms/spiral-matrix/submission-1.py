class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        c=len(matrix[0])
        r=len(matrix)
        t=0
        b=r-1
        l=0
        ri=c-1
        while t<=b and l<=ri:
            for i in range(l,ri+1):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                res.append(matrix[i][ri])
            ri-=1
            if t<=b:
                for i in range(ri,l-1,-1):
                    res.append(matrix[b][i])
                b-=1
            if l<=ri:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res

