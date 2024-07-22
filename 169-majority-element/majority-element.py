class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = 1 + hash_map.get(nums[i],0)
        
        n = size // 2

        for key,val in hash_map.items():
            if val > n:
                return key
        
        