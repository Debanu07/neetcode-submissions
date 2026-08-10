class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                a.append(i)
            elif i == ")":
                if len(a) == 0 or a[-1] != "(":
                    return False
                a.pop()

            elif i == "}":
                if len(a) == 0 or a[-1] != "{":
                    return False
                a.pop()

            elif i == "]":
                if len(a) == 0 or a[-1] != "[":
                    return False
                a.pop()
        if len(a)!=0:
            return False
        else:
            return True    