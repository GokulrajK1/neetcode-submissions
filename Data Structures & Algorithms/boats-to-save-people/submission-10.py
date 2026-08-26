class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # i = 0
        # j = len(people) - 1
        # boats = 0 
        # people.sort()

        # while i <= j:
        #     if people[i] + people[j] <= limit:
        #         boats += 1 
        #         i += 1 
        #         j -= 1
        #     else:
        #         j -= 1 
        #         boats += 1 
        
        # return boats 

        max_weight = max(people)
        weight_counts = [0] * max_weight 
        for person in people:
            weight_counts[person - 1] += 1 

        i = 0 
        j = max_weight - 1
        boats = 0 
        while i <= j:
            if weight_counts[i] == 0:
                i += 1 
            elif weight_counts[j] == 0:
                j -= 1
            elif i + 1 == limit:
                boats += weight_counts[i]
                weight_counts[i] = 0 
                i += 1 
            elif j + 1 == limit:
                boats += weight_counts[j]
                weight_counts[j] = 0 
                j -= 1 
            elif i == j:
                boats += (weight_counts[i] * (i + 1) // limit) 
                if (weight_counts[i] * (i + 1)) % limit > 0:
                    boats += 1 
                break 
            elif i + j + 2 <= limit:
                if weight_counts[i] < weight_counts[j]: 
                    boats += weight_counts[i] 
                    weight_counts[j] -= weight_counts[i]
                    weight_counts[i] = 0
                else: 
                    boats += weight_counts[j]
                    weight_counts[i] -= weight_counts[j] 
                    weight_counts[j] = 0
            else:
                boats += weight_counts[j]
                weight_counts[j] = 0 
                j -= 1 


        return boats 


        
                    
                    
        