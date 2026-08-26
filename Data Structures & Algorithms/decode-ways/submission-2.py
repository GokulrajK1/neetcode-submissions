class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        alphabet = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "E",
        "6" : "F", "7" : "G", "8" : "H", "9" : "I", "10" : "J", "11" : "K",
        "12" : "L", "13" : "M", "14" : "N", "15" : "0", "16" : "P", 
        "17" : "Q", "18" : "R", "19" :"S", "20" : "T", "21" : "U", "22" : "V",
        "23" : "W", "24" : "X", "25" : "Y", "26" : "Z"}

        def backtrack(i, memo):
            nonlocal n, alphabet
            if i == n:
                return 1

            if s[i] not in alphabet:
                return 0

            if i in memo:
                return memo[i]

            count = backtrack(i + 1, memo)

            if i < n - 1 and s[i:i+2] in alphabet:
                count += backtrack(i + 2, memo)
            
            memo[i] = count

            return count 

        return backtrack(0, {})

            