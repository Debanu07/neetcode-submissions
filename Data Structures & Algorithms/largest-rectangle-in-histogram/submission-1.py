class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        a=0
        s=[]
        for i in range(n+1):
            while s and (i==n or heights[s[-1]]>=heights[i]):
                h=heights[s.pop()]
                if len(s)==0:
                    w=i
                else:
                    w=i-s[-1]-1
                a=max(a,h*w)
            s.append(i)
        return a