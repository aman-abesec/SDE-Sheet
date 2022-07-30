#======================================================
#      N meetings in one room
#      https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
#      https://youtu.be/II6ziNnub1Q
#=========================================================
class Solution:
    def acc(self,ele):
        return ele[1]

    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        arr=[]
        for i in range(n):
            arr.append([start[i],end[i],i+1])
        arr.sort(key=self.acc)
        result=1
        e=arr[0][1]
        for i in range(1,len(arr)):
            if arr[i][0]>e:
                result+=1
                e=arr[i][1]
        return result
