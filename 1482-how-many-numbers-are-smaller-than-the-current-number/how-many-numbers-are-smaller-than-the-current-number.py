class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        for a brute force maybe we coudl iterate and then check 
        yes just take a pointer on each variable and themn use a nested loop
        to compare with all successive eles and then append to a res array
        '''
        res = []
        for i in nums:
            count = 0
            for num in nums:
                if num < i:
                    count+=1
            res.append(count)
        return res
        # time : O(n^2)
        # space : O(N)
