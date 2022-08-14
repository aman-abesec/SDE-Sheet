#=====================================================
#BFS of graph
#https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
#================================================================

from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def solve(self,s,adj,visited,result):
        q=deque()
        q.append(s)
        visited[s]=True
        while q:
            u=q.popleft()
            result.append(u)
            for v in adj[u]:
                if visited[v]==False:
                    visited[v]=True
                    q.append(v)
    def bfsOfGraph(self, V, adj):
        visited=[False for _ in range(V+1)]
        result=[]
        self.solve(0,adj,visited,result)
        return result
