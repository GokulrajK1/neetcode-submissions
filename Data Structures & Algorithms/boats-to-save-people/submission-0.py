class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people) - 1
        boats = 0 
        people.sort()

        while i <= j:
            if people[i] + people[j] <= limit:
                boats += 1 
                i += 1 
                j -= 1
            else:
                j -= 1 
                boats += 1 
        
        return boats 