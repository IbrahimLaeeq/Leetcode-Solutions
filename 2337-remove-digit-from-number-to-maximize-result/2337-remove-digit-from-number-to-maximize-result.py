class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        '''
        we compare the digit to be reomved and we have two cases:

        a) if the next digit is greater than the current digit
        then we shoudl delete the digit as we are maximizing/increasiing
        our no 

        i.e 1231 here "1" has 2 next to it so we delete the first "1"
        to obtain 231 which is the maximum answer as oppossed to 123

        b) if the next digit is smaller then we keep iterating until 
        we find a case where the next digit is greater

        c) if in all cases, teh , element present to the right of the
        "digit" is smaller than teh "digit" , then , we just remove the 
        last digit because we do have to remove a digit
        42121 digit  = "2"
        if we remove teh last 2 then , we get , 4211 as opposed to 
        4121 which we obtian if we remove the first two which gives us 
        a smaller answer

        we need to  keep track of the last_index because if we dont find 
        a case where the next ele or in this cae teh current pointer is
        greater than the digit then we woudl jsut set teh last pointer 
        here and then at the end we would just remove the "digit" at teh
        last_index and create a string in teh worst case 

        
        '''

        last_index = 0

        ''' 
        we iterate from one because we want to compare the curr ele
        with the previous ele and if the previous ele is a "digit"
        then we see taht if teh curr> prev then , removing , the prev 
        woud be good for us i.e maximizing so we would just go ahead and 
        do that
        '''
        for num in range (1,len(number)):

            if number[num-1]== digit:
                ''' 
                the digit is present one position to the left of teh
                curreent eleemenetn'''
                if int(number[num-1]) < int (number[num]):
                    return number[:num-1] + number[num:]
                else:
                    last_index = num - 1
            
            
           
            
            if number[-1] == digit:
                last_index = len(number) - 1
            
            '''
            we need this explicit check bc lets say
            123, digit = 3
            our for loop would not go to the "3" and it woudl return an incorrect
            answer because it only assumes that the "digit" is one position to
            the left of teh current pointer so when teh current pointer is at 
            '3" it would look for the digit one position to its left and it
            woudl find"2" there 

             if our digit is present at the lat of teh number then we just 
            set teh last incide to be at the last of the number
            '''
        return number[:last_index] + number[last_index+1:]
        