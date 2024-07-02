class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_seq = 0
        # create set to check for eles in O(1) time
        # sequence only starts when its previoius elemen
        # n - 1 ele is not present in set
        for i in set_nums:
            if (i-1) not in set_nums:
                # if its previous ele is not present in set
                # then we can start counting the length of 
                # the sequence
                count = 1
                while i + count in set_nums:
                    count +=1
                longest_seq = max(longest_seq, count)
        return longest_seq
                
        