class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in seen:
                return [seen[partner], i]
            seen[nums[i]] = i
            






# create a dictionary storing values and their index 

# partner = target - nums[i]
# has partner been seen before
# if yes return the index at where it was seen from the dictionary 
# if no store it in the dictionary and go back to the loop 

    




        
        