# Equations are given in the format A / B = k,
# where A and B are variables represented as strings,
# and k is a real number (floating point number).
# Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations,
# vector<double>& values, vector<pair<string, string>> queries ,
# where equations.size() == values.size(), and the values are positive.
# This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

# Subscribe to see which companies asked this question


# Since the number of nodes is small in the test cases
# DFS is better than BFS
# DFS: 38 ms
# BFS: 56 ms

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def bfs(v0, v1):
            visited = set([v0])
            queue = [(v0, 1.0)]
            while queue:
                thisNode, ans = queue.pop()
                if thisNode == v1:
                    return ans
                for variable in data[thisNode]:
                    if variable not in visited:
                        visited.add(variable)
                        queue.append((variable, ans * data[thisNode][variable]))
            return -1.0
                    
            
            
        if not equations:
            return [-1.0]* len(queries)
    
        data = {}
        ans = []
        for i in xrange(len(values)):
            value = values[i]
            v0, v1 = equations[i][0], equations[i][1]
            tmp = data.get(v0, {})
            tmp.update({v1:value})
            data[v0] = tmp
            tmp = data.get(v1, {})
            tmp.update({v0:1.0/value})
            data[v1] = tmp
    
        for query in queries:
            v0, v1 = query[0], query[1]
            if v0 not in data or v1 not in data:
                ans.append(-1.0)
            else:
                ans.append(bfs(v0, v1))
        return ans