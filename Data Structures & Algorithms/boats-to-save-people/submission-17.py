class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = [0] * (max(people) + 1)
        for person in people:
            weights[person] += 1

        counts = 0

        i = 0
        j = len(weights) - 1
        while i <= j:
            if weights[i] == 0:
                i += 1
                continue
            if weights[j] == 0:
                j -= 1
                continue 

            if i + j <= limit:
                if i == j:
                    counts += weights[i] // 2 + weights[i] % 2 
                    weights[i] = 0
                    continue
                boats = min(weights[i], weights[j])
                counts += boats
                weights[i] -= boats
                weights[j] -= boats 

            else:
                counts += weights[j]
                weights[j] = 0

        return counts



