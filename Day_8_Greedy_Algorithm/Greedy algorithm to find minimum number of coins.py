#======================================================
#      Find minimum number of coins that make a given value
#      https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
#      https://youtu.be/mVg9CfJvayM
#=========================================================
#User function Template for python3

class Solution:
    def minPartition(self, N):
        array=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ][::-1]
        result=[]
        for i in array:
            if i<=N:
                while i<=N:
                    result.append(i)
                    N-=i
        return result
