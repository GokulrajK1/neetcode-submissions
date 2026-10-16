class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0
        bill20 = 0
        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10:
                if bill5 == 0: return False
                bill5 -= 1
                bill10 += 1
            else:
                bill20 += 1
                if bill5 >= 3:
                    bill5 -= 3
                elif bill10 >= 1 and bill5 >= 1:
                    bill10 -= 1
                    bill5 -= 1
                else:
                    return False
        
        return True 