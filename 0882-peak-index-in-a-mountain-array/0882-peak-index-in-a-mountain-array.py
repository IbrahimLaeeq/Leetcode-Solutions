class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s= 0 
        e = len(arr)-1
        mid = (s + e ) // 2 
        # doing integer divison by "// " to avoid getting a float(decimal)
        # value as indices cant be in decimal format
        ''''
            for a value to be the peak value we need to make
            sure that its greater than its rightmost value
            and so we shall check if the value is smaller
            than its rightmost value and if so then  , we, 
            shall move the starting pointer ahead of our mid
            value by one point 

            the reason we don't check the previous value of the mid is 
            because we know that here for a peak the value should be greater
            than both its neighbours so even if it is less than one of its 
            neigbours then , it , means that the condition for it to 
            be a peak value is not satisfied 
        '''
        while s < e:  
            if arr[mid] < arr[mid+1]:
                s = mid+1
                mid = ( s  + e) // 2
                # we need to recalculate the mid at each step here 

            else:
                e = mid 
                mid =  ( s + e ) // 2
                # again recacluating our mid value
        return e