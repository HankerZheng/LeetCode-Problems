# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its
# next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

# Subscribe to see which companies asked this question

# Runtime: 64 ms

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return  0
        remain_list = [gas[i] - cost[i] for i,_ in enumerate(gas)]
        if sum(remain_list) < 0:
            return -1
        dp = [(0,0)] * len(gas)

        start = len(gas)-1
        current_sum = 0
        max_sum = current_sum
        index = start
        while start >= 0:
            current_sum += remain_list[start]
            if current_sum > max_sum:
                max_sum = current_sum
                index = start
            start -= 1
        res = 0
        gas_max = 0
        dp[-1] = (max_sum, index)
        for i,remain in enumerate(remain_list):
            if i == 0:
                if dp[-1][0]+remain > remain:
                    dp[i] = (dp[-1][0]+remain, index)
                else:
                    dp[i] = (remain,i)
                    index = i
            else:
                if dp[i-1][0]+remain > remain:
                    dp[i] = (dp[i-1][0]+remain, index)
                else:
                    dp[i] = (remain, i)
                    index = i
            if dp[i][0]>gas_max:
                gas_max, res = dp[i]
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.canCompleteCircuit([2,4,5],[5,4,2])

