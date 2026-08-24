class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''
        res1=[]
        for i in digits:
            a+=str(i)
        a1=int(a)
        res=a1+1
        while res:
            d=res%10
            res1.append(d)
            res=res//10
        res1.reverse()
        return res1
