#======================================================
#      Job Sequencing Problem
#      https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
#      https://youtu.be/LjPx4wQaRIs
#=========================================================
#User function Template for python3

class Solution:

    def acc(self,ele):
        return ele[2]
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        jobs=[]
        for i in range(n):
            jobs.append([Jobs[i].id,Jobs[i].deadline,Jobs[i].profit])
        jobs.sort(key=self.acc,reverse=True)
        mx=0
        for i in jobs:
            mx=max(mx,i[1])
        array=[-1]*mx
        result=0
        j=0
        for i in jobs:
            if array[i[1]-1]==-1:
                array[i[1]-1]=i[2]
                j+=1
                result+=i[2]
            else:
                c=i[1]-1
                while c>=0 and array[c]!=-1:
                    c-=1
                if c>=0 and array[c]==-1:
                    array[c]=i[2]
                    j+=1
                    result+=i[2]

        return [j,result]
