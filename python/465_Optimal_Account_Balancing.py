# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10.
# Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z.
# Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
# the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

# Note:

# A transaction will be given as a tuple (x, y, z). Note that x != y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        def update(valueSet, popOut, pushIn):
            popItem(valueSet, popOut)
            valueSet[pushIn] = valueSet.get(pushIn, 0) + 1

        def popItem(valueSet, popOut):
            if valueSet[popOut] == 1:
                valueSet.pop(popOut)
            else:
                valueSet[popOut] -= 1

        def getMinTrans(sources, sinks):
            cnt = 0
            for sink in sinks.keys():
                if sink in sources:
                    popItem(sources, sink)
                    popItem(sinks, sink)
                    cnt += 1
            if not sources:
                return sum(sinks.values()) + cnt
            elif not sinks:
                return sum(sources.values()) + cnt

            thisAns = float("inf")
            minSink, minSource = min(sinks), min(sources)
            if minSink < minSource:
                newSinks = dict(sinks)
                popItem(newSinks, minSink)
                for source in sources:
                    newSources = dict(sources)
                    update(newSources, source, source - minSink)
                    thisAns = min(thisAns, getMinTrans(newSources, newSinks))
            else:
                newSources = dict(sources)
                popItem(newSources, minSource)
                for sink in sinks:
                    newSinks = dict(sinks)
                    update(newSinks, sink, sink - minSource)
                    thisAns = min(thisAns, getMinTrans(newSources, newSinks))
            return thisAns + cnt + 1

        finalBalance = {}
        for src, dest, pay in transactions:
            finalBalance[src] = finalBalance.get(src, 0) - pay
            finalBalance[dest] = finalBalance.get(dest, 0) + pay
        sinks = {}
        sources = {}
        for balance in finalBalance.values():
            if balance > 0:
                sources[balance] = sources.get(balance,0) + 1
            elif balance < 0:
                sinks[-balance] = sinks.get(-balance,0) + 1
        if not sinks:
            return 0
        return getMinTrans(sources, sinks)


if __name__ == '__main__':
    sol = Solution()
    print sol.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]) == 1
    print sol.minTransfers([[2,0,5],[3,4,4]]) == 2
    print sol.minTransfers([[1,5,8],[8,9,8],[2,3,9],[4,3,1]]) == 4
    print sol.minTransfers([[0,1,10],[2,0,5]]) == 2
    print sol.minTransfers([[0,6,7],[0,7,7],[1,4,5],[1,5,4],[2,5,2],[3,7,1]]) == 6
    print sol.minTransfers([[0,6,7],[0,7,7],[1,4,4],[1,5,2],[2,5,3],[3,7,1]]) == 6