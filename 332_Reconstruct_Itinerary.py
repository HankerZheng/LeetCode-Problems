# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

from collections import defaultdict
class Solution(object):

    def findItinerary(self, tickets):
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        visit('JFK')
        return route[::-1]

    def findItinerary_mySol(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def helper(curState):
            if len(ans) == len(tickets) + 1:
                return 1

            for i, nextState in enumerate(destHash[curState]):
                if nextState[1]:
                    continue
                nextState[1] = 1
                ans.append(nextState[0])
                if helper(nextState[0]):
                    return 1
                ans.pop(-1)
                nextState[1] = 0
            return 0

        destHash = defaultdict(list)
        for ticket in tickets:
            destHash[ticket[0]].append([ticket[1], 0])
        for key in destHash:
            destHash[key].sort()
        curState = "JFK"
        ans = [curState]
        helper(curState)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])