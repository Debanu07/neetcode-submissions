class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        n=set(nums)
        for i in n :
            if i-1 not in n :
                l=1
                while i+l in n:
                    l+=1
                long=max(long,l)
        return long