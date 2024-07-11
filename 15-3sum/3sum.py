class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        getting a no which sint a duplicate and then
        looping to get a pair which isnt a duplicate
        '''
        res = []
        nums.sort()
        for idx , no in enumerate(nums):
            if idx > 0 and no == nums[idx-1]:
                continue
            
            l ,r = idx + 1 , len(nums) - 1
            while l < r:
                Ts = no + nums[l] + nums[r]
                if Ts>0:
                    r-=1
                elif Ts<0:
                    l+=1
                else:
                    res.append([no, nums[l] , nums[r] ])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res

        