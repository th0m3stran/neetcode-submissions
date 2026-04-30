class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Null condition, if the string lengths are different instant false 
        if len(s) != len(t):
            return False; 

        #defining my map 
        countS, countT = {},{} #inputs are string in array 

        for i in range (len(s)): # check every letter of the string length 
            #using a dictionary 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # increment each time it counts
            countT[t[i]] = 1+ countT.get(t[i], 0)
        return countS == countT
        # double == asks if countS and counT are the same 


        



# every letter should be added to the set 
# its unordered so we use set, can't set doesn't preserve duplicates 
# use a dictionary instead, counts how many times each letter appears 
# compare sets s and t that every letter exists 




        
        