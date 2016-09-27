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
#            the min-life of dungeon[m][n] is depend on dungeon[m-1][n] and 
#            dungeon[m][n-1]
# 
#   If we start from [0,0] and end at Princess, there would be 
#   If we start from Princess and end at [0,0], 
# 
# Time Complexity: O(M*N)


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        def cal_hp(maxhp,chp, this):
            n_chp = chp+this
            return [maxhp, n_chp] if n_chp>0 else [maxhp-n_chp, 0]

        dp = [[0,0] for row in dungeon]
        for col in xrange(len(dungeon[0])):
            for row in xrange(len(dungeon)):
                this = dungeon[row][col]
                if col==0 and row==0:
                    dp[row] = cal_hp(0,0,this)
                elif col==0:
                    dp[row] = cal_hp(dp[row-1][0], dp[row-1][1], this)
                elif row==0:
                    dp[row] = cal_hp(dp[row][0], dp[row][1], this)
                else:
                    down = cal_hp(dp[row-1][0], dp[row-1][1], this)
                    right = cal_hp(dp[row][0], dp[row][1], this)
                    dp[row] = min(down, right) if down[0]!=right[0] else max(down,right)
            print dp
        return dp[-1][0]+1

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