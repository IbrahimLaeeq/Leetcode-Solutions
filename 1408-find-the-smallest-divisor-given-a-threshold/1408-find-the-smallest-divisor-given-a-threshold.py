class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        basically what we do here is we apply binary 
        search on the smallest and the largest possible divisors
        '''
        import math
        l = 1
        r = max(nums)
        ''' 
        so here esetnialy we apply BS on the range of possible 
        divisors starting from zero and ending at the largest 
        value in the array because obvioiulsly the largest
        divisor cannot be greater than the largest value in 
        the array
        '''
        while l <= r:
            mid = (l + r) // 2
            sum = 0
            for num in nums:
                sum += math.ceil(num/mid)
                # doing this because they mentioned this in 2nd para
            if sum <= threshold:
                    r = mid - 1
            else:
                    l = mid + 1
        return l