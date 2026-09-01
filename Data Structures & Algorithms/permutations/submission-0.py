class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(p):
            if len(p)==len(nums):
                res.append(p[:])
                return
            for n in nums:
                if n in p:
                    continue
                p.append(n)
                dfs(p)
                p.pop()
        dfs([])
        return res