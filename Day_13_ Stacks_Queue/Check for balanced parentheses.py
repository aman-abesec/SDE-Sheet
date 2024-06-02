#====================================
#https://leetcode.com/problems/valid-parentheses/
#=====================================
class Solution:
    def isValid(self, s: str) -> bool:
        d={'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if i in ['{','[','(']:
                stack.append(i)
            else:
                if stack==[]:return False
                k=stack.pop()
                if k!=d[i]:return False
        if stack!=[]:return False
        return True
