class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        res=0
        while x>0:
            d=x%10
            res=res*10+d
            x=x//10
        res*=sign
        if res>(2**31)-1 or res<-1*(2**31):
            return 0
        return res 