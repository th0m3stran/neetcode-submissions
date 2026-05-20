class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Build dictionary 
        groups = {}

        for word in strs:               # every word goes through this same process: Sort, check if exists, add 
            key = "".join(sorted(word)) # sort the letters in a string and join 

            if key not in groups:   #first time seeing this key? 
                groups[key] = []    #create an empty list (box) for it 
            
            groups[key].append(word)    #if not first time time seeing key, toss the word into matching box 
        
        return list(groups.values())    #return all boxes as list of lists

            

        
        
