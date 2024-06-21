class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        we could do it the brute-force method but how do we ensure that 
        the eles are being sent to the end of the array we need some 
        method to ensure this

        ok for the solution with extra space we iterate througth the 
        origanl array and we compare each ele with zero and if that 
        ele is zero and then we nooo instead we compare and if the 
        curr ele is not a zero , then , we copy it to the array and 
        and this would maintian the relative order of the eles and
        then we coudl run another loop whihc would check if the 
        eles in the array are zero and then we could copy it to 
        the array but how will we make sure that we copy it after the
        previously copied eles and that it is not swapped / removes 
        the previous eles


        maybe we could store the indice of the last ele that we added
        to the new array

        i undersatnd the tewo pointer apparcho somehow we could compare 
        each ele with all its successive eles and if we see that

        andi f the curr pointer is zero and the incoming ele i.e
        successive ele is non-zero then we swap the two eles and
        then we continue this process , but , i dont understand 
        how we would move this pair of pointers

        here we move all teh non-zero eles to the left we can move 
        all non zero eles to the left or we coudl move all the 
        zero eles to the right but here we choose the former

        """

        left = 0 
        for right in range ( len(nums)):
            if nums[right]!=0:
                nums[right] , nums[left] = nums[left] , nums[right]
                '''
                swapping here is simpler as compared to how we do 
                it in other languages by creating a temp variable
                '''
                '''
                here casically if the successive or incoming ele
                is a non zero ele then we shift it to left 
                by swapping the value with the left pointer and 
                then the quesion i had earlier which was that how
                would we move this pair we just increment the
                values by one so here the main thing is the swapping
                happens when the incmoing or succsive ele at the 
                right pointer is a non zero ele so thats the chec
                '''
                left += 1
        return nums

    ''' 
    why are we not incrementing the right pointer here also why only the left
    pointer

    ans:
    it is being incrememted automatically in the for loop as we are using
    it to iterate through the array so , it , is incremented regardless
    and we just need to increment the left poinoter whenever we swap
    and the main condition for swappign is that the right pointer is
    a non-zero ele so it needs to be swapped with the left pointer
    otherwise if the right ele is a zero ele , then , there is no 
    need to swap it with the left ele
    '''


        