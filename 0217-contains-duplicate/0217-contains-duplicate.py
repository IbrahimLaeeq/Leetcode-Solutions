class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in nums:
            if i in count_dict:
                return True
            else:
                count_dict[i] = 1
        return False
        
        