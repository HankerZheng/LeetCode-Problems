# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms
# laid out in a 2D grid. Our valiant knight (K) was initially positioned
# in the top-left room and must fight his way through the dungeon to rescue
# the princess.

# The knight has an initial health point represented by a positive integer.
# If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health
# (negative integers) upon entering these rooms; other rooms are either empty
# (0's) or contain magic orbs that increase the knight's health (positive
# integers).

# In order to reach the princess as quickly as possible, the knight decides
# to move only rightward or downward in each step.


# Write a function to determine the knight's minimum initial health so that
# he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

# -2 (K)  -3  3
# -5  -10 1
# 10  30  -5 (P)

# Notes:

# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.


# Key Point: DP
#            the min-life of dungeon[m][n] is depend on dungeon[m+1][n] and 
#            dungeon[m][n+1]
# 
# 
# Time Complexity: O(M*N)


class Solution(object):
    def calculateMinimumHP_DP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:   return 0
        dp = [[float("inf") for j in xrange(len(dungeon[0]) + 1)] for i in xrange(len(dungeon) + 1)]
        dp[-1][-2] = dp[-2][-1] = 0
        
        i = len(dungeon) - 1
        while i >=0:
            j = len(dungeon[0]) - 1
            while j >= 0:
                dp[i][j] = max(0, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
                j -= 1
            i -= 1
        return dp[0][0] + 1


    def calculateMinimumHP_BFS_TLE(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:   return 0
        
        curHP = dungeon[0][0]
        minHP = min(0, curHP)
        heap = [(-minHP, curHP, 0, 0)]
        visited = {}
        while heap:
            thisState = heapq.heappop(heap)
            _, curHP, i, j = thisState
            minHP = -thisState[0]
            if (i,j) in visited and visited[(i,j)] > curHP:
                continue
            visited[(i,j)] = curHP
            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                return -minHP + 1
            if i + 1 < len(dungeon):
                nCurHP = curHP + dungeon[i+1][j]
                nMinHP = min(0, minHP, nCurHP)
                heapq.heappush(heap, (-nMinHP, nCurHP, i+1, j))
            if j + 1 < len(dungeon[0]):
                nCurHP = curHP + dungeon[i][j+1]
                nMinHP = min(0, minHP, nCurHP)
                heapq.heappush(heap, (-nMinHP, nCurHP, i, j+1))
        return None
if __name__ == "__main__":
    test = Solution()
    query = [
        [[0,-5,-3],  [-2,4,-5], [1,-6,-7]], # 11
        [[1]], #1
        [[1,-4,3]], #4
        [[1,-1,1,-1],
         [-1,1,-1,1]], #1
        [[1,-3,3],[0,-2,0],[-3,-3,-3]], #3
    ]

    for q in query:
        ans = test.calculateMinimumHP(q)
        print ans