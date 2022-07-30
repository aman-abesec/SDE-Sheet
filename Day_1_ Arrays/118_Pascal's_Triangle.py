#======================================================
#           118. Pascal's Triangle
#  https://leetcode.com/problems/pascals-triangle/
#  https://youtu.be/6FLvhQjZqvM
#=========================================================
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]]
        if numRows==1:
            return result
        for j in range(1,numRows):
            box=[1]
            for i in range(1,j):
                box.append(result[j-1][i-1]+result[j-1][i])
            box.append(1)
            result.append(box)
        return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[0]*(i+1) for i in range(numRows)]
        for j in range(numRows):
            result[j][0]=result[j][j]=1
            for i in range(1,j):
                result[j][i]=result[j-1][i-1]+result[j-1][i]
        return result
