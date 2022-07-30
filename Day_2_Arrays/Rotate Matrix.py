#======================================================
#           48. Rotate Image
#  https://leetcode.com/problems/rotate-image/
#  https://youtu.be/Y72QeX0Efxw
#=========================================================
# Method-1:
# Approach:>
# Take another matrix Make Rom col of second matrix
# S:O(n^2)
# T:O(n^2)

l=3
new_mat=[[0]*l for i in range(l)]
mat=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(l):
    for j in range(l):
        new_mat[j][l-i-1]=mat[i][j]
print(new_mat)


#Approach:>
    # 1>take transpose of matrix
    # 2>Revere each row of matrix
#S:O(1)
#T:O(n^2)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][len(matrix[0])-1-j]  =  matrix[i][len(matrix[0])-1-j],matrix[i][j]  #         return matrix
