#=====================================================
#Topological sort
#https://practice.geeksforgeeks.org/problems/topological-sort/1
#================================================================

class Solution:
    #Function to return list containing vertices in Topological order.
    def solve(self,u,visited,result):
        visited[u]=True
        for v in adj[u]:
            if visited[v]==False:
                self.solve(v,visited,result)
        result.append(u)
    def topoSort(self, V, adj):
        result=[]
        visited=[False for _ in range(V)]
        for u in range(V):
            if visited[u]==False:
                self.solve(u,visited,result)
        return result[::-1]
