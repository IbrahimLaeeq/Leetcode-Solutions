class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        res_r = n-1
        res = [0] * n
        while l < r:
            val_l, val_r = abs(nums[l]), abs(nums[r])
            if val_l > val_r:
                res[res_r] = val_l*val_l
                l += 1
            else:
                res[res_r] = val_r*val_r
                r -= 1
            res_r -= 1
                
        res[0] = nums[l]*nums[l]
        return res