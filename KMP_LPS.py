def lpsBuilder(s):
    """
    Given a target string, build the Longest Prefix Suffix array.
    lps
    """
    lps = [0] * len(s)
    lpsIdx = 1
    prefixIdx = 0
    while lpsIdx < len(s):
        while lpsIdx < len(s) and s[lpsIdx] == s[prefixIdx]:
            lps[lpsIdx] = prefixIdx + 1
            prefixIdx += 1
            lpsIdx += 1
        if prefixIdx < len(s) and prefixIdx != 0:
            # s[lpsIdx] != s[prefix]
            prefixIdx = lps[prefixIdx-1]
        else:
            lpsIdx += 1
    return lps

if __name__ == '__main__':
     print lpsBuilder("aabaaaabac")
     print lpsBuilder("ababaabc")
     print lpsBuilder("aaaa")