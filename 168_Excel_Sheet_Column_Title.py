# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

# Runtime: 46ms
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = []
        while n:
            n, rem = divmod(n - 1, 26)
            title.append(lookup[rem])
            
        return "".join(title[::-1])


if __name__ == '__main__':
    sol = Solution()
    print sol.convertToTitle(1)
    print sol.convertToTitle(2)
    print sol.convertToTitle(10)
    print sol.convertToTitle(26)
    print sol.convertToTitle(27)
    print sol.convertToTitle(701)