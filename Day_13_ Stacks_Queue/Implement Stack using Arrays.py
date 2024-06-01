#======================================
#https://www.geeksforgeeks.org/problems/implement-stack-using-array/1
#=======================================
class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        #add code here
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.arr!=[]:
            topEle=self.arr[-1]
            self.arr.pop()
            return topEle
        return -1
