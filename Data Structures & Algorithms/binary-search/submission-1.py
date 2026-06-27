class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 #left pointer 
        r = len(nums) - 1 #right pointer

        while l <= r:
            m = (l+r) // 2
            if nums[m] > target: #moving the right pointer
                r = m - 1
            elif nums[m] < target: #moving the left pointer
                l = m + 1
            else: # if not either that means m = target
                return m 

        return -1 # target not found in array 
        
# using midpoint we deduce and reduce the numbers we need to iterate through reducing time comp 
# only works in sorted arrays.