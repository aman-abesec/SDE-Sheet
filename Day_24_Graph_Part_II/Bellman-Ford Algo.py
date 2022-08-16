#=====================================================
#Distance from the Source (Bellman-Ford Algorithm)
#https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0?fbclid=IwAR2_lL0T84DnciLyzMTQuVTMBOi82nTWNLuXjUgahnrtBgkphKiYk6xcyJU
#================================================================

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        #Inplace 0f 100000000 we can also write math.inf
        dist=[100000000 for _ in range(V)]
        dist[S]=0
        l=len(adj)
        for _ in range(V-1):
            for i in range(l):
                u,v,wt=adj[i]
                if dist[v]>dist[u]+wt:
                    dist[v]=dist[u]+wt
        return dist
