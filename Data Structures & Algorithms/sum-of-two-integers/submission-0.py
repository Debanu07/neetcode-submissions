class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        max_int=0x7FFFFFFF
        while b!=0:
            a1=(a^b)& mask
            b1=((a & b)<<1) & mask
            a=a1
            b=b1
        if a<=max_int:
            return a 
        else:
            return ~(a^mask)