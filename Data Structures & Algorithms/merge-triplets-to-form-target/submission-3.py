class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [float("-inf"), float("-inf"), float("-inf")]
      
        for i, val in enumerate(target):
            if curr == target:
                return True
            if curr[i] == target[i]:
                continue
            for triplet in triplets:
                if triplet[i] == target[i]:
                    print(triplet, "T")
                    for j, old_val in enumerate(curr):
                        new_val = max(old_val, triplet[j])
                        curr[j] = new_val
                    break
            print(curr)
                    

        return curr == target 


