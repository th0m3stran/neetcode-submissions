class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #length sof wthe two strings must be the same 
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)      # loops through each letter adding a count to seen
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT 
            



        