class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        correct = [False, False, False]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue 
      
            if triplet[0] == target[0]:
                correct[0] = True
            if triplet[1] == target[1]:
                correct[1] = True
            if triplet[2] == target[2]:
                correct[2] = True

        return correct == [True, True, True]

            