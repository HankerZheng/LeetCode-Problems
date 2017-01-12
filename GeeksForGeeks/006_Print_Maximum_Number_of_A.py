# Reference: http://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/

# Imagine you have a special keyboard with the following keys: 
# Key 1:  Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it
#                  after what has already been printed. 

# If you can only press the keyboard for N times (with the above four
# keys), write a program to produce maximum numbers of A's. That is to
# say, the input parameter is N (No. of keys that you can press), the 
# output is M (No. of As that you can produce).
# Examples:
# 
# Input:  N = 3
# Output: 3
# We can at most get 3 A's on screen by pressing 
# following key sequence.
# A, A, A
# 
# Input:  N = 7
# Output: 9
# We can at most get 9 A's on screen by pressing 
# following key sequence.
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
# 
# Input:  N = 11
# Output: 27
# We can at most get 27 A's on screen by pressing 
# following key sequence.
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A, 
# Ctrl C, Ctrl V, Ctrl V

def printMostA(n):
    """
    :tpye n: int
    :rtype: int
    """
    def optimalMultiple(k):
        """
        return the best multiple on given press k
        """
        if k < 7:
            return k - 1
        if k in history:
            return history[k]
        thisAns = 0
        for thisCase in xrange(3, 7):
            thisAns = max(thisAns, optimalMultiple(k - thisCase) * (thisCase - 1))
        history[k] = thisAns
        return thisAns


    if n < 7:
        return n
    ans = 0
    history = {}
    for baseA in xrange(3, 7):
        ans = max(ans, baseA * optimalMultiple(n - baseA))
    return ans

if __name__ == '__main__':
    assert printMostA(3) == 3
    assert printMostA(7) == 9
    for i in xrange(8, 21):
        print "press number is %d, maximum number of A is %d" % (i, printMostA(i))
    print printMostA(79)