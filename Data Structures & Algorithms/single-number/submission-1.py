class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        new = set() #creating unordered set

        for i in nums: #for every number in nums
            if i in new: # i exists in set? 
                new.remove(i)
            else: # i does not exist in set 
                new.add(i)

        return list(new)[0]