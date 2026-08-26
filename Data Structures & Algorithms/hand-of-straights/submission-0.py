class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1 

        sorted_counts = sorted(counts)
        for card in sorted_counts:
            if counts[card] == 0:
                continue 
            c = counts[card]
            for i in range(card, card + groupSize): 
                if counts.get(i, 0) < c:
                    return False 
                counts[i] -= c

        return True
