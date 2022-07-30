#======================================================
#      74. Search a 2D Matrix
#   https://leetcode.com/problems/search-a-2d-matrix/
#   https://youtu.be/ZYpYur0znng
#=========================================================
#S-O(1)
#T-O(n^2)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==target:
                    return True
        return False

#S-O(1)
#T-O(logn) r*c
# Approach:> row and column at any index will be mid//column_len and mid%column_len
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        n=r*c
        beg=0
        end=n-1
        while beg<=end:
            mid=(beg+end)//2
            m=matrix[mid//c][mid%c]
            if m==target:
                return True
            elif m>target:
                end=mid-1
            else:
                beg=mid+1
        return False
