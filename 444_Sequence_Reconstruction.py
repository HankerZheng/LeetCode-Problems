# Example 1:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]

# Output:
# false

# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:

# Input:
# org: [1,2,3], seqs: [[1,2]]

# Output:
# false

# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

# Output:
# true

# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:

# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

# Output:
# true
# Show Company Tags
# Show Tags
# Show Similar Problems

from collections import defaultdict
class Solution(object):
    def sequenceReconstruction_EdgeCheck(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        edgeSet = set()
        for seq in seqs:
            prevNode = seq[0]
            for nextNode in seq[1:]:
                edgeSet.add((prevNode, nextNode))

        prevNode = org[0]
        for nextNode in org[1:]:
            if (prevNode, nextNode) not in edgeSet:
                return False
        return True

    def sequenceReconstruction_TopologicalSort(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        def findNoSource():
            thisAns = []
            lastAns = noSource[0]
            for thisNode in edgeSet[lastAns]:
                inDegSet[thisNode] -= 1
                if inDegSet[thisNode] == 0:
                    thisAns.append(thisNode)
            return thisAns

        inDegSet = {}
        edgeSet = defaultdict(set)
        for seq in seqs:
            if not seq:
                continue
            startNode = seq[0]
            inDegSet[startNode] = inDegSet.get(startNode, 0)
            edgeSet[startNode] = edgeSet.get(startNode, set())
            for endNode in seq[1:]:
                if endNode not in edgeSet[startNode]:
                    inDegSet[endNode] = inDegSet.get(endNode, 0) + 1
                    edgeSet[startNode].add(endNode)
                startNode = endNode

        if len(inDegSet) != len(org):
            return False

        checkIdx = 0
        noSource = []
        for thisNode in inDegSet:
            if inDegSet[thisNode] == 0:
                noSource.append(thisNode)
        while checkIdx < len(org):
            if len(noSource) != 1:
                return False
            startPoint = noSource[0]
            noSource = findNoSource()
            if not startPoint or startPoint != org[checkIdx]:
                return False
            checkIdx += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    # print sol.sequenceReconstruction_TopologicalSort([1,2,3], [[1,2],[1,3],[2,3]])
    # print sol.sequenceReconstruction_TopologicalSort([1,2], [[1,2],[1,2]])