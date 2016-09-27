# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def find_no_prerequisite(available_course):
            higher = set([high for (high, low) in available_relations if low in available_course])
            res = available_course - higher
            return res, higher

        res = []
        available_course = set()
        available_relations = set()
        # init available_course and available_relations
        for prerequisite in prerequisites:
            available_course.add(prerequisite[0])
            available_course.add(prerequisite[1])
            available_relations.add((prerequisite[0], prerequisite[1]))

        # Topological sort the node
        while available_course:
            no_incomes, available_course = find_no_prerequisite(available_course)
            for this_work in no_incomes:
                res.append(this_work)
            if len(res) >= numCourses:
                return True
            if not no_incomes:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.canFinish(2, [[1,0]])
    print sol.canFinish(2, [[1,0], [0,1]])
    print sol.canFinish(2, [])