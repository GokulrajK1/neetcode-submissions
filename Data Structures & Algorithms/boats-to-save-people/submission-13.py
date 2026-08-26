class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Solution 1 
        # people.sort()
        # n = len(people)
        # i = 0 
        # j = n - 1 
        # boats = 0
        # while i <= j:
        #     if people[i] + people[j] <= limit:
        #         boats += 1 
        #         i += 1 
        #         j -= 1 
        #     else:
        #         boats += 1 
        #         j -= 1 

        # return boats

        # Solution 2 
        max_weight = max(people)
        weight_counts = [0] * (max_weight + 1)
        for person in people:
            weight_counts[person] += 1 
        i = 1 
        j = max_weight 
        boats = 0
        while i <= j:
            if weight_counts[i] == 0:
                i += 1 
            elif weight_counts[j] == 0:
                j -= 1
            elif i == limit:
                boats += weight_counts[i]
                weight_counts[i] = 0
                i += 1 
            elif j == limit:
                boats += weight_counts[j]
                weight_counts[j] = 0
                j -= 1 
            elif i == j:
                if i + i > limit:
                    boats += weight_counts[i]
                else:
                    boats += weight_counts[i] // 2 + weight_counts[i] % 2 
                break 
            elif i + j <= limit:
                if weight_counts[i] > weight_counts[j]:
                    boats += weight_counts[j]
                    weight_counts[i] -= weight_counts[j]
                    weight_counts[j] = 0 
                    j -= 1
                else:
                    boats += weight_counts[i]
                    weight_counts[j] -= weight_counts[i]
                    weight_counts[i] = 0 
                    i += 1 
            else:
                boats += weight_counts[j]
                weight_counts[j] = 0
                j -= 1

        return boats 
