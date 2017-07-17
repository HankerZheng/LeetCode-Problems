# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Subscribe to see which companies asked this question

# Runtime: 84 ms

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        string = ""
        for ch in path:
            if ch == "/":
                if string == "..":
                    res and res.pop(-1)
                elif string != "." and string:
                    res.append(string)
                string = ""
            else:
                string+=ch
        if ch != "/":
            if string == "..":
                res and res.pop(-1)
            elif string != "." and string:
                res.append(string)
        res = "/".join(res)
        return "/"+res
if __name__ == '__main__':
    sol = Solution()
    print sol.simplifyPath("/..")


