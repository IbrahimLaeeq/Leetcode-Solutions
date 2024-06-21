class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        non decreasing basically means that the eles are in 
        increasing order but the eles can be same like:
        [1,,2,2,3,4,,4]

        here the main thing is we have to determine the eles
        that are duplicates and then the shifting procesure is simple
        where we shift the eles that are not equal to this duplicate
        ele to the left thus shifting this duplicate ele to the right
        but we have to modify this to make sure that one instance of
        the duplicate ele is present as is  because in shifting all
        the instances of said duplicate ele will be shifted to the
        right so we have to avoid that and we also have to come
        up with a logic to return the "k" value because it isnt 
        as simple bc we cant use a normal for loop to get the no
        of eles in the array

        the main trick here is that for swapping each time we would need
        to determine teh duplicate ele and then swap all eles which are
        not equal to this duplicate ele to the left but how do we 
        determine this duplicate ele in each iteration?

        ok so if the eles in the rigth pointer are equal to the ele 
        in the left pointer then it means that boht the left and right 
        pionter eles are equal so we should send this right pointer ele
        to the end right?
        '''


        '''
        we iterate and see that the left pointer gives us the indice
        and we use the right pointer to determine a unique value
        which we can then shift towards the left and how do we determine a
        unqiue value we compare the value at the right poniter
        to its antecedent and if they are the same then it means 
        we have a duplicate value otherwise we havea  unique value
        '''
        left = 1
        for right in range(1,len(nums)):
            ''' 
            the value at the zero indice doesnt need to be 
            changed so that's why we start the loop from one
            '''
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                ''' 
                this means we have a duplicate value and we send 
                it to the place where we have our left indice because
                that is what gives us the indice for the duplicate
                values
                '''
                left+=1
                ''' 
                we increment teh left pointer because we have now placed
                an element at this indice so we increment it to get
                a new indice where we can place the next unqiue value
                '''
        return left
        ''' 
        the left pointer gives us the indice for the duplicate eles
        so we can return that as it will also tell us about the 
        no of duplicate eles we have in our array
        '''
        '''
        we wont need to return left+1 because lets say 
        [1,1,2]
           L R
           whenver we swap then in the if statement we increment the left
           pointer so here then 
        [1,2,1]
             L
             R
            now when the code goes the for loop then it woudl go out
            of bounds but our left pointer is at indice two which also 
            ahppens to be the no of unqiue els in the arry so we can
            go ahead and return that
            '''