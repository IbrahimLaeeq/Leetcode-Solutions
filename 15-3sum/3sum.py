class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() # O(nlogn)
        for idx , no in enumerate(nums): #O(n)
            l = idx + 1
            r = len(nums) - 1
            while l < r:# O(n)
                Ts = no + nums[l] + nums[r]
                if Ts < 0:
                    l+=1
                elif Ts >0:
                    r-=1
                else:
                    res.add((no  , nums[l] , nums[r]))
                    l+=1
        return res
        '''
        time : O(nlogn) + O(n^2) = O(n^2)
        space : O(N)
        '''