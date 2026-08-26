class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Solution 1 
        people.sort()
        n = len(people)
        i = 0 
        j = n - 1 
        boats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                boats += 1 
                i += 1 
                j -= 1 
            else:
                boats += 1 
                j -= 1 

        return boats