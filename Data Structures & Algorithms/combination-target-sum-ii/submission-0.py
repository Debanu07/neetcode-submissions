class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(start,target,path):
            if target==0:
                res.append(path[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i]>target :
                    break
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1,target-candidates[i],path)
                path.pop()
        dfs(0,target,[])
        return res