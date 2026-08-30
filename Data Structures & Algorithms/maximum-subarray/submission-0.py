class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        t=0
        res=nums[0]
        for n in nums:
            if t<0:
                t=0
            t+=n
            res=max(res,t)
        return res            