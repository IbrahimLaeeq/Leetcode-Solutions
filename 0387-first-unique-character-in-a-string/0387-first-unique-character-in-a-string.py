class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        maybe in a map we have order so we create a map and then 
        iterate or we culd create the map iteravitely no that would
        not work bc we might haea "v" at teh second indice and then 
        we would also have one at the last indice

        crerate a map by looping and hten in the second iteratoin 
        we would iterate throught the map and the first char 
        whcih has a count i.e value of oned woudl be returned

        we woudl get its indice by maybe passing it to the original string a
        and then using. getindeix or something
        no need to do this just iteate thorght hte string again 
        and see the counta gainst a speicif cindice and then we could return taht 
        first ele whose count is one

        '''

        # creating a map
        map = {}
        for i in range (len(s)):
            map[s[i]] = 1 + map.get(s[i], 0)
        
        for idx , no in enumerate(s):
            if map[no] == 1:
                return idx
        return -1

        