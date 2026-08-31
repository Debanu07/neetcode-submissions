class Solution:
    def isHappy(self, n: int) -> bool:
        def rec(n1):
            s=0
            while n1>0:
                d=n1%10
                s+=d**2
                n1=n1//10
            return s
        s1=set()

        while n!=1:
            if n in s1:
                return False
            s1.add(n)
            n=rec(n)
        return True
            
