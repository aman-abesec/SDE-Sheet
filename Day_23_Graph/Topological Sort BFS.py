#=====================================================
#Topological sort
#https://practice.geeksforgeeks.org/problems/topological-sort/1
#================================================================

from collections import deque
class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        result=[]
        indegree=[0 for _ in range(V)]
        for i in range(V):
            for v in adj[i]:
                indegree[v]+=1
        q=deque()
        for j in range(V):
            if indegree[j]==0:
                q.append(j)
        while q:
            u=q.popleft()
            result.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        # print(result)
        return result
