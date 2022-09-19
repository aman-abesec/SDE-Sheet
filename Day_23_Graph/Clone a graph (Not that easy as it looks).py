#=====================================================
#133. Clone Graph
#https://leetcode.com/problems/clone-graph/om-data-stream/
#https://www.youtube.com/watch?v=xZ9st62u2Yk&ab_channel=Codebix
#================================================================
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:return None
        q=deque()
        hash_map={}
        q.append(node)
        hash_map[node.val]=Node(node.val)
        while q:
            n=q.popleft()
            for data in n.neighbors:
                if data.val not in hash_map:
                    hash_map[data.val]=Node(data.val)
                    q.append(data)
                hash_map[n.val].neighbors.append(hash_map[data.val])
        return hash_map[node.val]
