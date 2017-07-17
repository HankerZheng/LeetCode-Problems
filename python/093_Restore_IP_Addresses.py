# Given a string containing only digits, restore it by
# returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# Subscribe to see which companies asked this question

# Runtime: 72ms


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def partition_helper(ans, start, choke):
            if choke == 4:
                for info in ans:
                    if not info or int(info) > 255 or (info[0]=="0" and len(info)>1):
                        return
                res.append(".".join(ans))
            elif start<len(s) and choke == 3:
                partition_helper(ans+[s[start:]], -1, choke+1)
            elif start<len(s) and s[start]=="0":
                partition_helper(ans+[s[start:start+1]],start+1, choke+1)
            elif start<len(s):
                partition_helper(ans+[s[start:start+1]],start+1, choke+1)
                partition_helper(ans+[s[start:start+2]],start+2, choke+1)
                partition_helper(ans+[s[start:start+3]],start+3, choke+1)
        res = []
        partition_helper([], 0, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.restoreIpAddresses("12345")
    print sol.restoreIpAddresses("25525511135")
    print sol.restoreIpAddresses("010010")