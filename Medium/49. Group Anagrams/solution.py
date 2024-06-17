class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # default keys to an empty list

        for word in strs:
            chars = [0] * 26 # 26 indexes set to 0
            for c in word: # loop through each character in current word
                chars[ord(c) - ord('a')] += 1 # find index value of character and increment
            ans[tuple(chars)].append(word) # use tuple to use chars array as key, append the word

        return ans.values() # returns values of dictionary
