class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 

        hand_count = {}
        for h in hand:
            hand_count[h] = hand_count.get(h, 0) + 1

        for h in sorted(hand_count):
            h_count = hand_count[h]
            if h_count == 0:
                continue
            for i in range(groupSize):
                if h + i not in hand_count:
                    return False
                if hand_count[h + i] < h_count:
                    return False
                hand_count[h + i] -= h_count 

        for h, count in hand_count.items():
            if count != 0:
                return False

        return True 
            