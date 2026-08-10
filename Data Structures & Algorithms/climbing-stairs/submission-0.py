class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def cs(n):
            if n<=2:
                return n 
            if dp[n]!=0:
                return dp[n]
            dp[n]=cs(n-1)+cs(n-2)
            return dp[n]
        return cs(n)