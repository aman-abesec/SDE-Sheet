#=====================================================
#Detect cycle in an undirected graph
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
#================================================================

from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		def cycle(s,visited,adj):
            q=deque()
            q.append([s,-1])
            visited[s]=True
            while q:
                u,prev=q.popleft()
                for v in adj[u]:
                    if visited[v]==False:
                        q.append([v,u])
                        visited[v]=True
                    elif visited[v]==True and prev!=v:
                        return True
            return False
        def solve(v,adj):
            visited=[False for _ in range(v+1)]
            for i in range(0,v):
                if visited[i]==False:
                    if cycle(i,visited,adj):
                        return True
            return False

        return solve(V,adj)
