class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)): #first index 
            for j in range(i + 1, len(nums)): #second index of the same array (start, stop)
                difference = target - nums[i] #target is given, we are at first index and we compare rest of the list to index 0 
                if difference == nums[j]: #if the difference value is correct 
                    return [i,j] # return the index on outer loop, then inner loop which this occurs


            