# Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

# Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

# Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

# Examples:

# Input: "WRRBBW", "RB"
# Output: -1
# Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

# Input: "WWRRBBWW", "WRBRW"
# Output: 2
# Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

# Input:"G", "GGGGG"
# Output: 2
# Explanation: G -> G[G] -> GG[G] -> empty 

# Input: "RBYYBBRRB", "YRBGB"
# Output: 3
# Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

# Note:
# You may assume that the initial row of balls on the table won't have any 3 or more consecutive balls with the same color.
# The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
# The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
# Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def getBalls(balls):
            """
            Convert the init given board string into a ball list.
            Each element of the list is in the form of [color, ballCnt]
            This function can automatically clear the 3 consective balls with
            the same color in the given string.

            >>> getBalls("RRBBBGYYWWWYB")
            [["R", 2], ["B", 3], ["G", 1], ["B", 1]]
            """
            ballList = []
            for ball in balls:
                if not ballList or ballList[-1][0] != ball:
                    if ballList and ballList[-1][1] >= 3:
                        ballList.pop(-1)
                    ballList.append([ball, 1])
                elif ball == ballList[-1][0]:
                    ballList[-1][1] += 1
            return ballList
        
        def combineBalls(balls1, balls2):
            """
            Combine 2 sets of balls together.

            >>> combineBalls({"R": 1}, {"R": 1, "G": 1})
            {"R": 2, "G": 1}
            """
            ans = dict(balls1)
            for key, value in balls2.items():
                if key in ans:
                    ans[key] += value
                else:
                    ans[key] = value
            return ans
        
        def cntBalls(balls):
            """
            Count the number of balls we have chosen.
            Since there is only 5 colors in the game, this function can be done in O(1) time.
            """
            return sum(balls.values())

        def updateAns(ans1, ans2):
            """
            Compare two different solution to the sub-problem,
            and return the better one.
            If `ans1` has fewer balls and `ans1` can be formed by the balls given,
            then just return `ans1`, else we return `ans2`
            Therefore, `ans1` should always be the new soluton, while `ans2` the old.
            """
            if cntBalls(ans1) < cntBalls(ans2) and checkAvailable(ans1, ballsInHand) >= 0:
                return ans1
            return ans2
        
        def checkAvailable(balls, ballsInHand):
            """
            Check whether current balls is available according to the given balls.
            Since there is only 5 colors in the game, this function can be done in O(1) time.
            """
            for key, value in balls.items():
                if balls[key] != 0:
                    if key not in ballsInHand:
                        return -1
                    if ballsInHand[key] < value:
                        return -1
            return sum(balls.values())

        def memorySearch(start, end):
            if end < start:
                return {}
            elif (start, end) in history:
                return history[(start, end)]
            elif start == end:
                # There is only one color in the sub-problem
                return {ballsTable[start][0]: 3 - ballsTable[start][1]}
            elif start + 1 == end:
                # There is only two color in the sub-problem
                return combineBalls(memorySearch(start, start), memorySearch(end, end))
            # When there are more than 3 color in the sub-problem
            thisAns = {"R":float("inf")}
            firstColor, lastColor = ballsTable[start][0], ballsTable[end][0]
            # The first possible Solution is to split the balls into 2 parts and finish both of them seperately
            for k in xrange(start, end):
                thisBalls = combineBalls(memorySearch(start, k), memorySearch(k+1, end))
                thisAns = updateAns(thisBalls, thisAns)
            # The second possible Solution is to clear the first and the last balls in the end
            if firstColor == lastColor:
                toAdd = max(0, 3 - ballsTable[start][1] - ballsTable[end][1])
                thisBalls = combineBalls(memorySearch(start+1, end-1), {firstColor: toAdd})
                thisAns = updateAns(thisBalls, thisAns)
            # The third possible Solution is to clear the first and the last balls in the end with
            # one ball in the middle
            if firstColor == lastColor and 1 in (ballsTable[start][1], ballsTable[end][1]):
                idx = start + 1
                while idx < end:
                    if ballsTable[idx][0] == firstColor and ballsTable[idx][1] == 1:
                        thisBalls = combineBalls(memorySearch(start + 1, idx - 1), memorySearch(idx + 1, end - 1))
                        thisAns = updateAns(thisBalls, thisAns)
                    idx += 1
            history[(start, end)] = thisAns
            return thisAns
            
        # Initialization
        ballsTable = getBalls(board)
        ballsInHand = {}
        for ball in hand:
            ballsInHand[ball] = ballsInHand.get(ball, 0) + 1
        history = {}
        # print ballsTable
        length = len(ballsTable)
        return checkAvailable(memorySearch(0, length - 1), ballsInHand)

if __name__ == '__main__':
    sol = Solution()
    # print sol.findMinStep("RBYYBBRRB","YRBGB") == 3
    # print sol.findMinStep("WWRRBBWW", "WRBRW") == 2
    # print sol.findMinStep("G", "GGGGG") == 2
    # print sol.findMinStep("WRRBBW", "RB") == -1
    # print sol.findMinStep("RRWWRRW", "RR") == 2
    # print sol.findMinStep("RWYWRRWRR", "YRY") == 3
    # print sol.findMinStep("WYWRRW", "YRY") == 3
    # print sol.findMinStep("GGRRGRRG", "RRYBB") == 2
    # print sol.findMinStep("WWYYWYYWWRRYWY", "RWWWY") == 4
    print sol.findMinStep("WWYRBGGWYRGBBWYRYGBRYWGBRYWGGRYWBGBGRWYYGBRYWYGBRYWGBYRRGBYWYRYGBRYYGYRBWYRYGBBGGRYWBWBYRYBGYRWYBGYR", "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGGGGGGGGYYYYYYYYYYYYYYYBBBBBBBBBBBBBBBBBBBBB")