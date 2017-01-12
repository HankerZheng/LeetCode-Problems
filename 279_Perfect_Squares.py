# 279. Perfect Squares   QuestionEditorial Solution  My Submissions
# Total Accepted: 57001
# Total Submissions: 165352
# Difficulty: Medium
# Contributors: Admin
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def numSquares(self, n):
        def getSmallerSquare(num):
            i = 1
            while i*i <= num:
                yield i*i
                i += 1

        queue = {n}
        new_queue = set()
        count = 0
        while queue:
            for num in queue:
                for square in getSmallerSquare(num):
                    if square == num:   return count + 1
                    new_queue.add(num - square)
            count += 1
            queue = new_queue
            new_queue = set()
        return n
