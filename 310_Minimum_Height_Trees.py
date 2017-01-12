# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Show Hint 

from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        # traverse the edges and create the graph in graphEdges - O(E + V)
        graphEdges = [[] for i in xrange(n)]
        for node1, node2 in edges:
            graphEdges[node1].append(node2)
            graphEdges[node2].append(node1)
        # create the degree list for each node                - O(V)
        # init the oneDegNodes
        degreeList = [0] * n
        oneDegNodes = []
        for nodeName, neighbors in enumerate(graphEdges):
            degreeList[nodeName] = len(neighbors)
            if len(neighbors) == 1:
                oneDegNodes.append(nodeName)

        # Main loop to kick out the nodes with only one degree - O(E)
        nodesLeft = n
        while nodesLeft != len(oneDegNodes):
            newList = []
            # for each node with oneDeg, kick it out from graph, and find the new node with only one degree
            for oneDegNode in oneDegNodes:
                for nei in graphEdges[oneDegNode]:
                    degreeList[nei] -= 1
                    if degreeList[nei] == 1:
                        newList.append(nei)
                nodesLeft -= 1
            oneDegNodes = newList
        return oneDegNodes

if __name__ == '__main__':
    sol = Solution()
    print sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
