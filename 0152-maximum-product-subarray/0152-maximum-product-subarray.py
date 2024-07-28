class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        curr_prod = 1

        for i in range(len(nums)):
            curr_prod *= nums[i] 
            max_prod = max(curr_prod, max_prod)
            if curr_prod == 0:
                curr_prod = 1
            
            # resetting the prodcut if it becomes one

        curr_prod = 1
        # resetting again for the reverse pass

        for i in range(len(nums) - 1 , -1 , -1 ): # start , end , jump
        # by default goes from left to right so we have to specify
            curr_prod *= nums[i] 
            max_prod = max(curr_prod, max_prod)
            if curr_prod == 0:
                curr_prod = 1
            # resetting the prodcut if it becomes one
        
        return max_prod
        