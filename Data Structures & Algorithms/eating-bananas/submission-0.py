import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            mid=(l+r)//2
            c=0
            for i in piles:
                c+=math.ceil(i/mid)
            if c>h:
                l=mid+1
            else:
                r=mid-1
        return l