class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[1]*n
        pl=1
        ps=1
        for i in range(n):
            l[i]*=pl
            pl=pl*nums[i]
        for i in range(n-1,-1,-1):
            l[i]*=ps
            ps=ps*nums[i]
        return l