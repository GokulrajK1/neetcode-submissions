class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0: return False 

        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1 

        for number in hand:
            start = number
            while counts.get(start - 1, 0) != 0:
                start -= 1 
            while start <= number:
                while counts.get(start, 0) != 0:
                    for i in range(start, start + groupSize):
                        if counts.get(i, 0) == 0:
                            return False 
                        counts[i] -= 1
                start += 1 

        return True

            

