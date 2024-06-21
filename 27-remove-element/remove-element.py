class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        so esentially tell the no of eles which are not equal 
        to teh given val which can be determined by just
        using a for loop for comparsion and then shift all instances
        of the given val to the end of the array and return both 
        the array and the no of eles in the array that are not equal to
        the 'val'
        '''
        '''
        we could use two pointers here for shifting the val to the
        right hand side and we could use a for loop to get
        the count of the eles not equal to the "val"

        either send the val to the right side or an easier way
        woudl be to send all eles that are not equal to 
        "val" to the left hand side so we iterate and the right pointer
        and whenver we encounter an ele in the right pointer that is
        not equal to "val" then , we , send it to the left hand side and
        automatically the "val " is being sent to the right hand side
        because of this
        '''
        count = 0
        for i in nums:
            if i != val:
                count+=1
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[right] , nums[left] = nums[left] , nums[right]
                left+=1
        
        return count
