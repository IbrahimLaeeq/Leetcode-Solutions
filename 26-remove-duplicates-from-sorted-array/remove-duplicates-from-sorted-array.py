class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        for  r in range(1,len(nums)):
            if nums[l] != nums[r]:
                l +=1
                nums[l] = nums[r]
                # shifting the right val towards the left
        return l + 1