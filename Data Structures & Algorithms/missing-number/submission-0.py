class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums) #unordered set return the list 
        n = len(nums)
        for i in range (n+1): #check every number, incremen
            if i not in num_set: #if 
                return i
        