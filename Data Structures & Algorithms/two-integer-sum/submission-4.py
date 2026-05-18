class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)): #first index 
            for j in range(i + 1, len(nums)): #second index of the same array (start, stop)
                difference = target - nums[i]
                if difference == nums[j]:
                    return [i,j]


            




#essentially we start at the first index 
# difference - value and we find that value in the loop exists or not iterating one by one 
# if doesnt exist we go to 2nd index as a comparison and loop through the ones after 
# once found, we return the index where the two occurs 