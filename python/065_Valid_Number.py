# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# "2e4.1" => flase
# "00.000" => true
# "3.24e000" => true
# ".24e000" => true
# "24000." => true
# "e24e000" => false
# "e24." => false
# "e" => false
# "." => false
# "2e" => false
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.

# Runtime: 97ms
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = s.strip()
        if not string:
            return False
        e_flag, point_flag, num_flag = 0,0,0
        for i,num in enumerate(string):
            if num<='9' and num>='0':
                num_flag = 1
            elif num == '.':
                if e_flag or point_flag:
                    return False
                point_flag = 1
            elif num == 'e':
                if e_flag or not num_flag:
                    return False
                e_flag = 1
                num_flag = 0
                point_flag = 1
            elif num == '-' or num=='+':
                if i!=0 and string[i-1]!='e':
                    return False
            else:
                return False
        if not num_flag:
            return False
        return True





if __name__ == '__main__':
    sol = Solution()
    print sol.isNumber("")
    print sol.isNumber("  ")
    print sol.isNumber(" 123 ")
    print sol.isNumber(" 1.2e2 ")
    print sol.isNumber(" 3e2.2")
    print sol.isNumber(" .22")
    print sol.isNumber(" 22.")
    print sol.isNumber(" e22.")
    print sol.isNumber("O +")