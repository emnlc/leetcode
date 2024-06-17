class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create maps for both strings s and t
        sMap = {}
        tMap = {}

        # cannot be anagrams if the lengths are different
        if len(s) != len(t):
            return False

        # loop through the length of a string
        for i in range(len(s)):
            # add characters from respective string to their map
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        # return equivalence of maps
        return sMap == tMap