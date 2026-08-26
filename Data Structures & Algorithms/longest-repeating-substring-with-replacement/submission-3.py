class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = list(set(list(s)))
        max_length = 0
        for char in chars:
            left = 0 
            count = 0 
            for right in range(len(s)):
                if s[right] == char:
                    count += 1 
                else:
                    while right - left + 1 > count + k:
                        if s[left] == char:
                            count -= 1 
                        left += 1 

                length = right - left + 1 
                if length > max_length:
                    max_length = length 

        return max_length

                


                


                

                
            

            