class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hsh = set()
        for n in nums:
            if n in hsh:
                return True
            hsh.add(n)
        return False
        