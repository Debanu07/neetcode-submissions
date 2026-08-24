class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        h=len(heights)
        r=h-1
        area=0
        while l<r:
            h1=min(heights[l],heights[r])
            a=h1*(r-l)
            area=max(a,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area 