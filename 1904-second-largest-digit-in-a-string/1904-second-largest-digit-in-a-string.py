class Solution:
    def secondHighest(self, s: str) -> int:
        '''
        for finding the lowest and the higest digit that would 
        be somewhat easy we coudl just iterate and compare the 
        current digit with the previous digit and then just 
        store the min/max no depending upon our requiremetn

        one way woudl be to get the distinct characters using a 
        set and then just sort them and return teh second elemenet
        because in sorted order but that would only work if we have only 
        three elemeent if ew have four elements i.e 1347 then here  
        , the , second largest ele is "4 ' but it is present at the 
        seond indice and not the first indice , so  , there must 
        be a formula for getting teh indice

        maybe sorting wont work bc we also have characters (enligh words)
        SORTING WOULD WORK HERE

        for creating set we dont need to add all the elements 
        we iterate througth the input string and if we see that the 
        ele at the current indice is a digit , then , we add it to 
        the set other-wise we dont add it to the set 
        
        dude after soring teh largest ele woudl be present at the 
        end so to return teh second largest we coudl just return -2 indice
        '''
        
        l = []
        for i in range(len(s)):
            if s[i].isnumeric():
                l.append(s[i])

                '''
                here basically we are appeidign only nos to our new list
                '''
        l = list(set(l))
        l.sort()
        '''
        we convert our list to a set to remove the duplicate eles 
        and then , we  , convert this to a list again so we can 
        get indices and stuff bc a set doenst have any order in 
        it so we cannto access eles in a set through their indices
        '''
        if len(l) < 2:
            return  -1
            '''
            if len is less than 2 then it mean theat we only have one
            ele so we cannot compare it with anytihing else

            e.g: 1111

            here we dont have a second largest element
            '''
        ele = int(l[-2])
        return ele