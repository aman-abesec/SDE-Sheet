#======================================================
#      Fractional Knapsack
#      https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
#      https://youtu.be/F_DDzYnxO14
#=========================================================

class Solution:
    def acc(self,ele):
        return ele.value/ele.weight
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        Items.sort(key=self.acc,reverse=True)
        curr=0
        result=0
        for i in Items:
            if i.weight+curr<=W:
                result+=i.value
                curr+=i.weight
            else:
                c=W-curr
                result+=(i.value/i.weight)*c
                curr+=c
                break
        return result
