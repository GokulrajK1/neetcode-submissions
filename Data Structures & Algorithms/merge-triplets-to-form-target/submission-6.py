class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue 
            res[0] = target[0] == triplet[0] if not res[0] else res[0] 
            res[1] = target[1] == triplet[1] if not res[1] else res[1] 
            res[2] = target[2] == triplet[2] if not res[2] else res[2] 

        return res == [True, True, True]
            