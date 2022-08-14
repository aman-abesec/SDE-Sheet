#=====================================================
#Detect cycle in an undirected graph
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
#================================================================

from collections import deque
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        indegree=[0 for _ in range(V+1)]
        for i in range(V):
            for v in adj[i]:
                indegree[v]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            u=q.popleft()
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
            count+=1
        if count!=V:return True
        return False
