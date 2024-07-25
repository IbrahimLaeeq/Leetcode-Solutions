class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True: 
            mid = (left + right) // 2
            res = guess(mid)

            if res > 0: 
                left = mid + 1
            elif res < 0: 
                right = mid - 1
            else: 
                return mid
            
# Time -> O(log n)
# Space -> O(1)