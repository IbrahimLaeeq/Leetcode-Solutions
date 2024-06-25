class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in nums:
            arr1.append(i)
            arr2.append(i)
        return arr1 + arr2
