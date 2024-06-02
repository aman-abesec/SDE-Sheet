#======================================
#https://www.geeksforgeeks.org/problems/next-larger-element-1587115620
#========================================
class Solution:
    def nextLargerElement(self,arr,n):
        ans=[]
        stack=[]
        stack.append(n-1)
        ans.append(-1)
        for i in range(n-2,-1,-1):
            while stack!=[] and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if stack==[]:ans.append(-1)
            else:ans.append(arr[stack[-1]])
            stack.append(i)
        return ans[::-1]
