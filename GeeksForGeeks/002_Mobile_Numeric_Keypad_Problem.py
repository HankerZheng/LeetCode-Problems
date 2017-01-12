# Reference: http://www.geeksforgeeks.org/mobile-numeric-keypad-problem/
# Given the mobile numeric keypad. You can only press buttons that are up, left, right or down to the current button. You are not allowed to press bottom row corner buttons (i.e. * and # ).
# Given a number N, find out the number of possible numbers of given length.

# Examples:
# For N=1, number of possible numbers would be 10 (0, 1, 2, 3, …., 9)
# For N=2, number of possible numbers would be 36
# Possible numbers: 00,08 11,12,14 22,21,23,25 and so on.
# If we start with 0, valid numbers will be 00, 08 (count: 2)
# If we start with 1, valid numbers will be 11, 12, 14 (count: 3)
# If we start with 2, valid numbers will be 22, 21, 23,25 (count: 4)
# If we start with 3, valid numbers will be 33, 32, 36 (count: 3)
# If we start with 4, valid numbers will be 44,41,45,47 (count: 4)
# If we start with 5, valid numbers will be 55,54,52,56,58 (count: 5)
# {'1','2','3'},
# {'4','5','6'},
# {'7','8','9'},
# {'*','0','#'}

def countKeyboard(n):
    cntEnd13 = 2
    cntEnd46 = 2
    cntEnd79 = 2
    cntEnd2 = 1
    cntEnd5 = 1
    cntEnd8 = 1
    cntEnd0 = 1
    for i in xrange(n - 1):
        tmp13 = cntEnd2 * 2 + cntEnd46 + cntEnd13 # 13
        tmp46 = cntEnd13 + cntEnd5 * 2 + cntEnd79 + cntEnd46 # 46
        tmp79 = cntEnd46 + cntEnd8 * 2 + cntEnd79 # 79
        tmp2 = cntEnd13 + cntEnd5 + cntEnd2 # 2
        tmp5 = cntEnd2 + cntEnd46 + cntEnd8 + cntEnd5 # 5
        tmp8 = cntEnd5 + cntEnd79 + cntEnd0 + cntEnd8 # 8
        tmp0 = cntEnd8 + cntEnd0 # 0
        cntEnd13, cntEnd46, cntEnd79, cntEnd2, cntEnd5, cntEnd8, cntEnd0 = \
                tmp13, tmp46, tmp79, tmp2, tmp5, tmp8, tmp0
    return cntEnd13 + cntEnd46 + cntEnd79 + cntEnd2 + cntEnd5 + cntEnd8 + cntEnd0

if __name__ == '__main__':
    for i in xrange(1, 10):
        print countKeyboard(i)