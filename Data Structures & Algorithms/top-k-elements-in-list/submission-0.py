class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a=[]
        for i,c in d.items():
            a.append([c,i])
        a.sort(reverse=True)
        r=[]
        for i in range(k):
            r.append(a[i][1])
        return r