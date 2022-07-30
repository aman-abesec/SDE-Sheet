#======================================================
#      37. Sudoku Solver
#      https://leetcode.com/problems/sudoku-solver/
#
#=========================================================
# def isvalid(r,c,mat):
#     if r>=0 and r<len(mat) and c>=0 and c<len(mat[0]):
#         return True
#     return False
#
# def solve(r,c,mat,vis,ans,s):
#     direction=[[1,0,'D'],[-1,0,'U'],[0,-1,'L'],[0,1,'R']]
#     if r==len(mat)-1 and c==len(mat[0])-1:
#         ans.append(s)
#         return
#     for i in direction:
#         row=r+i[0]
#         col=c+i[1]
#         if isvalid(row,col,mat) and [row,col] not in vis:
#             vis.append([row,col])
#             solve(row,col,mat,vis,ans,s+i[2])
#             vis.remove([row,col])
#             # solve(row,col,mat,vis,ans,s)
#
# mat=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# ans=[]
# vis=[[0,0]]
# s=''
# solve(0,0,mat,vis,ans,s)
# print(ans)


# l=map(int,input().split())
# c=0
# while c in l:
#     c+=1
# print(c)

# for _ in range(int(input())):
#     l=int(input())
#     a=list(map(int,input().split()))
# print(7^2)

def isvalid(r,c,mat):
    if r>=0 and r<len(mat) and c>=0 and c<len(mat[0]):
        return True
    return False

def solve(r,c,d1,d2,mat,vis,ans,s):
    direction=[[1,0,'D'],[0,1,'R']]#[-1,0,'U'],[0,-1,'L'],[0,1,'R']]
    if r==d1 and c==d2:
        ans.append(s)
        return
    for i in direction:
        row=r+i[0]
        col=c+i[1]
        if isvalid(row,col,mat) and [row,col] not in vis:
            vis.append([row,col])
            solve(row,col,d1,d2,mat,vis,ans,s+i[2])
            vis.remove([row,col])
            # solve(row,col,mat,vis,ans,s)

n,m=map(int,input().split())
mat=[[0]*n for k in range(m)]
ans=[]
vis=[]
solve(0,0,0,0,mat,vis,ans,'')
print(ans)

# for _ in range(int(input())):
#     l=list(map(int,input().split()))
#     ans=[]
#     vis=[[l[0],l[1]]]
#     solve(l[0],l[1],l[2],l[3],mat,vis,ans,'')
#     print(ans)
