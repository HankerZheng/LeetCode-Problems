# A string such as "word" contains the following abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume that m <= 21, n <= 1000, and log2(n) + m <= 20.
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def getAbbr(abbrIdx):
            idx = 0
            abbr = []
            while idx < len(target):
                mask = 1 << idx
                if mask & abbrIdx:
                    count = 0
                    while idx < len(target) and mask & abbrIdx:
                        idx += 1
                        count += 1
                        mask = 1 << idx
                    abbr.append(str(count))
                else:
                    abbr.append(target[idx])
                    idx += 1
            return abbr

        def checkWord(abbr, word):
            iabbr, iword = 0, 0
            while iabbr < len(abbr) and iword < len(word):
                if abbr[iabbr].isdigit():
                    iword += int(abbr[iabbr])
                    iabbr += 1
                elif abbr[iabbr] == word[iword]:
                    iabbr += 1
                    iword += 1
                else:
                    return True
            return False

        def checkUnique(abbr):
            ans = True
            for word in sameLength:
                ans = ans and checkWord(abbr, word)
            return ans

        sameLength = []
        for word in dictionary:
            if len(word) == len(target):
                sameLength.append(word)
        
        if not sameLength: return str(len(target))

        curAns = target
        for abbrIdx in xrange(2**len(target)):
            abbr = getAbbr(abbrIdx)
            if len(abbr) < len(curAns) and checkUnique(abbr):
                curAns = abbr
        return "".join(curAns)


    def minAbbreviation_bit(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def getWordNum(word):
            ans = 0
            idx = 0
            while idx < len(word):
                ans += (word[idx] != target[idx]) << idx 
                idx += 1
            return ans
        
        def getAbbr(abbrIdx):
            idx = 0
            abbr = []
            while idx < len(target):
                mask = 1 << idx
                if not mask & abbrIdx:
                    count = 0
                    while idx < len(target) and not mask & abbrIdx:
                        idx += 1
                        count += 1
                        mask = 1 << idx
                    abbr.append(str(count))
                else:
                    abbr.append(target[idx])
                    idx += 1
            return abbr
            
        sameLength = []
        for word in dictionary:
            if len(word) == len(target):
                sameLength.append(getWordNum(word))
        if not sameLength:  return str(len(target))
        ans = target
        for i in xrange(1<<len(target)):
            if all([i & wordNum for wordNum in sameLength]):
                tmp = getAbbr(i)
                if len(tmp) < len(ans):
                    ans = tmp
        return "".join(ans)

if __name__ == '__main__':
    sol = Solution()
    print sol.minAbbreviation_bit("apple",  ["applt","hpple"])
    # trieGraph = TrieGraph( ["applt","hpple"])
    # print trieGraph.find(0, "apple")