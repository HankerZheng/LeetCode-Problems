# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Note:
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

class Codec:
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        splitChar = "`"
        converChar = "@"
        ans = []
        for string in strs:
            for char in string:
                if char == splitChar or char == converChar:
                    ans.append(converChar + char)
                else:
                    ans.append(char)
            ans.append(splitChar)
        return "".join(ans)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        splitChar = "`"
        converChar = "@"
        res = []
        ans = []
        i = 0
        while i < len(s):
            if s[i] == converChar:
                ans.append(s[i + 1])
                i += 2
            elif s[i] == splitChar:
                res.append("".join(ans))
                ans = []
                i += 1
            else:
                ans.append(s[i])
                i += 1
        return res

