class Solution:
    def isPalindrome(self, s: str) -> bool:
        # placeholder for new and corrected string 
        new = ""

        for char in s: #for every character in the string 
            if char.isalnum():  # consider alphanumerics only 
                new += char.lower() #lowercase it and return new string 
         
        left = 0
        right = len(new) - 1

        while left < right: 
            if new[left] != new[right]: #pointer values in new string 
                return False;
            left += 1 #move left pointer right 
            right -=1 #move right pointer left 
        return True
            
            

            
        