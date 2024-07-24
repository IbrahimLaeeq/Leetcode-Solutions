class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        size = len(nums) // 3
        # integer divison analogus to ceil function
        e1, e2 ,c1 ,c2 = 0,0,0,0
        res = []
        for i in nums:
            if i == e1:
                c1+=1
            elif i == e2:
                c2 +=1
            elif c1 == 0 and i != e2:
                e1 = i 
                c1 =1
            elif c2 == 0 and i !=e1:
                e2 = i
                c2 =1
            else:
                c1 -=1
                c2 -=1
            # this gives us the two majority eles but doesnt give us their
            # real count
        c1  , c2 = 0 , 0 
        for i in nums:
            if i == e1:
                c1 +=1 
            elif  i == e2:
                c2 +=1
        # we get the actual counts at this point
        if c1 > size:
            res.append(e1)
        if c2 > size:
            res.append(e2)
        return res
        
    
        