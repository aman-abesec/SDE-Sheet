#========================================================
#      474. Ones and Zeroes
#https://leetcode.com/problems/ones-and-zeroes/
#https://www.youtube.com/watch?v=PSYnD_yz-l8&ab_channel=CodewithAlisha
#=========================================================
#Method-1
class Solution:
    def solve(self,arr,l0,l1,l):
        if l==0:return 0
        c0=arr[l-1].count('0')
        c1=arr[l-1].count('1')
        if l0-c0>=0 and l1-c1>=0:
            return max(1+self.solve(arr,l0-c0,l1-c1,l-1),self.solve(arr,l0,l1,l-1))
        else:
            return self.solve(arr,l0,l1,l-1)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        return self.solve(strs,m,n,l)

#Method-2
dp=[]
class Solution:
    def solve(self,arr,l0,l1,l):
        global dp
        if l==0:return 0
        if l0==0 and l1==0: return 0
        if dp[l0][l1][l]!=-1:return dp[l0][l1][l]
        c0=arr[l-1].count('0')
        c1=arr[l-1].count('1')
        if (l0-c0)>=0 and (l1-c1)>=0:
            dp[l0][l1][l]=max(1+self.solve(arr,l0-c0,l1-c1,l-1),self.solve(arr,l0,l1,l-1))
            return dp[l0][l1][l]
        else:
            dp[l0][l1][l]=self.solve(arr,l0,l1,l-1)
            return dp[l0][l1][l]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        global dp
        dp=[[[-1 for p in range(l+1)] for i in range(101)] for _ in range(101)]
        return self.solve(strs,m,n,l)

#Method-3
class Solution:
    def solve(self,arr,l0,l1,l):
        dp=[[[0 for ___ in range(l1+1)] for __ in range(l0+1)] for _ in range(l+1)]
        for i in range(1,l+1):
            c0=arr[i-1].count('0')
            c1=arr[i-1].count('1')
            for m in range(l0+1):
                for n in range(l1+1):
                    if (m-c0)>=0 and (n-c1)>=0:
                        dp[i][m][n]=max(1+dp[i-1][m-c0][n-c1],dp[i-1][m][n])
                    else:
                        dp[i][m][n]=dp[i-1][m][n]
        return dp[l][l0][l1]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        return self.solve(strs,m,n,l)

# ["10","0001","111001","1","0"]
# 5
# 3
# ["10","0","1"]
# 1
# 1
# ["11111","100","1101","1101","11000"]
# 5
# 7
# ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
# 9
# 80
# ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"]
# 44
# 39
