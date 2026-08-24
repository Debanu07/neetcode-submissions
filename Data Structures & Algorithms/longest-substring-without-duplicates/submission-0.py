class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l=0
       c=0
       s1=set()
       for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            s1.add(s[r])
            c=max(c,r-l+1)
       return c 