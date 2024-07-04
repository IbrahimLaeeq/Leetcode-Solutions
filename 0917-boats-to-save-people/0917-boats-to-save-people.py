class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people) - 1
        while left<=right:
            if left == right:
                boats +=1
                break
                # tihs would be the last person so we would break 
                
            elif people[left]+ people[right] <= limit:
                # both people can go in the boat in this case
                left +=1
                right -=1
                boats +=1
            else:
                # if sum of both is greater than limit , then ,
                # process only the right(greater) ele
                boats +=1
                right -=1
        return boats
        
        