#======================================================
#      50. Pow(x, n)
#   https://leetcode.com/problems/powx-n/
#   https://youtu.be/l0YC3876qxg
#=========================================================
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result=1.0
        if n>0:
            for i in range(n):
                result*=x
            return result
        elif n==0:
            return 1.0
        else:
            for i in range(-n):
                result*=(1/x)
            return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return (x**(n))


#T-O(lon)
#S-O(1)
#Approach:>
    # Cheque power is positive or negative
    # if n is even:
    #     base=base*base
    #     n=n//2
    # else:
    #     ans=ans*base
    #     n=n-1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        nn=n
        if nn<0:
            nn=-1*nn
        while nn>0:
            if nn%2==0:
                x=x*x
                nn=nn//2
            else:
                ans*=x
                nn=nn-1
        if n<0:
            return 1/ans
        return ans
