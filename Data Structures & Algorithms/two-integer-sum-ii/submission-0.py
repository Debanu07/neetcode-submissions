class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p={}
        for i,num in enumerate(numbers):
            d= target-num
            if d in p:
                return[p[d]+1,i+1]
            p[num]=i
        