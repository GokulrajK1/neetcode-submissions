class Solution:
    def decodeString(self, s: str) -> str:
        numbers = []
        strings = []

        string = ""
        number = ""

        for char in s:
            if char.isalpha():
                string += char
            elif char.isdigit():
                number += char
            elif char == "[":
                strings.append(string)
                numbers.append(int(number))
                string = ""
                number = ""
            else:
                print("d", char)
                print(string)
                n = numbers.pop()
                decoded = string * n 
                prefix = ""
                if strings:
                    prefix = strings.pop()
                number = ""
                string = prefix + decoded

        strings.append(string)

        return "".join(strings)

        



