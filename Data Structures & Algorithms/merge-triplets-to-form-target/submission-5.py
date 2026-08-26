class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [float("-inf"), float("-inf"), float("-inf")]
        for i in range(3):
            for triplet in triplets:
                if triplet[i] == target[i]:
                    can_merge = True
                    for j in range(3):
                        if res[j] == target[j] and max(triplet[j], res[j]) != target[j]:
                            can_merge = False

                    if can_merge:
                        res = [max(triplet[0], res[0]), max(triplet[1], res[1]), max(triplet[2], res[2])]

            if res[i] != target[i]:
                return False

        return True