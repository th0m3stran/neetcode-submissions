class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Has this number been seen yet?
        seen =  set()

        for i in nums: 
            if i in seen: #value of i in seen yet? 
                return True 
            seen.add(i) #otherwise if not yet seen, add this to i, then reloop again 

        return False  #if only appears once return true. 

        