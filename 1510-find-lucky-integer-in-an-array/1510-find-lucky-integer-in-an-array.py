class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ''' 
        we can use a hash map here
        '''
        res = [-1]
        Set = set(arr)

        for i in Set:
            if i == arr.count(i):
                res.append(i)
        
        return max(res)
