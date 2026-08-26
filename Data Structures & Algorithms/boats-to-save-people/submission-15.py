class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counts = [0] * (max(people) + 1)
        for person in people:
            counts[person] += 1

        i = 1
        j = len(counts) - 1

        print(counts)
        
        boats = 0

        while i <= j:

            if counts[i] == 0:
                i += 1

            elif counts[j] == 0:
                j -= 1 

            elif i + j > limit:
                boats += counts[j]
                j -= 1 

            elif i + j <= limit:
                combined = min(counts[i], counts[j])
                if i == j:
                    boats += combined // 2 + combined % 2 
                    counts[i] = 0
                    continue
                
                boats += combined 
                counts[i] -= combined
                counts[j] -= combined 

        return boats

            


        