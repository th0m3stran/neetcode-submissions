class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: #Number in array list 
            if num in seen: #If number contains duplicate 
                return True # True
            seen.add(num) #Otherwise add the number, then goes back to L4
        return False; #If all numbers unique then it will return false.