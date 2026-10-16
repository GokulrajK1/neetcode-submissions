class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0: return False 

        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1 

        min_card = min(counts)
        max_card = max(counts)


        nums = 0

        for h in range(min_card, max_card + 1):

            if h not in counts:
                continue

            if counts[h] == 0:
                continue

     
            
            for i in range(groupSize - 1):
                if h + i + 1 not in counts:
            
                    return False 

                if counts[h + i + 1] < counts[h]:
              
                    return False

                counts[h + i + 1] -= counts[h]

            nums += counts[h]
            counts[h] = 0

        return nums == len(hand) // groupSize

            

