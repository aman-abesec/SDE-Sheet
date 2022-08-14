#=====================================================
#785. Is Graph Bipartite?
#https://leetcode.com/problems/is-graph-bipartite/
#================================================================

from collections import deque
class Solution:
    def solve(self,s,color,adj):
        q=deque()
        q.append(s)
        color[s]=0
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v in color and color[v]==color[u]:
                    return False
                elif v not in color :
                    q.append(v)
                    color[v]=1-color[u]
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        for i in range(len(graph)):
            if i not in color:
                if self.solve(i,color,graph)==False:
                    return False
        return True
