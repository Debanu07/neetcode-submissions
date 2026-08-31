class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1.isdigit() is True and num2.isdigit() is True:
            i=int(num1)
            j=int(num2)
            z=i*j
            z1=str(z)
            return z1
        else:
            return 0
