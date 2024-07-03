class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        store the counts in a hash map on teh first 
        loop and then once we have the hash map 
        run another loop on the input and see that
        for this specific character if its count in 
        the map is equal to one
        '''
        '''
        1. we use a defaultdict bc we are mapping from 
        char to int so here we could just define that
        we are mapping to an int to avoid the key errors 
        when the key doesnt exist before in the hasp map
        i.e we encounter an ele for the first
        time in the string
        '''
        hash_map = defaultdict(int)
        # char -> int
        for i in s:
            hash_map[i] +=1
        
        for idx , no in enumerate(s):
            if hash_map[no] == 1:
                return idx
        return -1