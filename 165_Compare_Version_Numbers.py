# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three",
# it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Runtime: 49ms

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1list = version1.split('.')
        ver2list = version2.split('.')
        len1, len2 = len(ver1list), len(ver2list)
        minlength = min(len1, len2)
        i = 0
        while i < minlength:
            if int(ver1list[i]) > int(ver2list[i]):
                return 1
            elif int(ver1list[i]) < int(ver2list[i]):
                return -1
            else:
                i+=1
        if len1 > len2:
            while i < len1:
                if int(ver1list[i]) > 0:
                    return 1
                i+=1
        else:
            while i < len2:
                if int(ver2list[i]) > 0:
                    return -1
                i+=1
        return 0



if __name__ == '__main__':
    sol = Solution()
    print sol.compareVersion("1.0", "1.0.0.0.1")