class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        '''
        either we coudl remove the digits one by one and store 
        the result and tehn just call the max funciton on it
        but this woudl be the brute force apparoach 

        eg:
        for 1231 we weoudl get 123 and 231 and we would store them
        and tehn we could just call teh max function on it like
        max (all variables) and then just return the max variable
        '''
        ans = 0 
        for i , dig in enumerate (list(number)):
            '''
            the enumerate funciton returns / gives us both the indice
            and also teh no present at the current indice so it
            returns a pair of (indice, number) but to use this 
            function we need a list because only lists have indices
            and we cannot use the enumerate function on a string
            like we are given in teh question bc strings dont have
            indices so basically the reaon for using enumerate here is
            that we need to compare the no at each point with the given
            digit so we use the enumerate function to simmplify 
            things otherwise we could jsut do the normal interation
            too after converting it into a list but we could not iterate
            on it whilst it was still a string , and , once we encounter
            our "digit" we woudl remove that by creating two substrings one
            that consists of all teh eles before the digit and one that 
            consisits of all the eles after the digit adn tehn we woudl 
            append them and then compare that with the previous no that
            we got and store the max of them and then return it . 
            '''
            if dig == digit:
                ans = max(ans, int (number[:i]  + number[i+1:]))
            '''
            we use teh max funncotin becuase we want to compare the 
            previous value and the current value adn only store teh 
            maximum value out of those two and we use the stirngs
            slicing here

            [:i] this gives us a substring from the start of teh
            number to the current indice i.e current indice is not 
            inlcuded in the sub string basically the value at "i" 
            isn ot included in the sub-string and then

            [i+1:] this gives us a substring from teh i+1 indice till 
            the end of the string
            '''
        return str (ans)

        