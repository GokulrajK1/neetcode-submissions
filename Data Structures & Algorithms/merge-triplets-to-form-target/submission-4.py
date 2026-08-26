class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        obtained = [False, False, False]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            obtained[0] = triplet[0] == target[0] if not obtained[0] else True
            obtained[1] = triplet[1] == target[1] if not obtained[1] else True
            obtained[2] = triplet[2] == target[2] if not obtained[2] else True

        return obtained == [True, True, True]


