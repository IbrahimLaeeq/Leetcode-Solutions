class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max = cur = sum(nums[:k])
        for i in range(len(nums)- k):
            cur = cur - nums[i] + nums[i+k]
            if cur > max:
                max = cur
        return max/k
            


        