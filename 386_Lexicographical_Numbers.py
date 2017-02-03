# Given an integer n, return 1 - n in lexicographical order.

# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def addNewNumber(currentNum, upperBound):
            ansList.append(currentNum)
            for i in xrange(10):
                newNum = currentNum * 10 + i
                if newNum > upperBound:
                    break
                addNewNumber(newNum, upperBound)
        if n < 10:
            return range(1,n+1)
        ansList = []
        for i in xrange(1, 10):
            addNewNumber(i, n)
        return ansList