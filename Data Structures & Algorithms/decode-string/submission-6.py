class Solution:
    def decodeString(self, s: str) -> str:
        strings = []
        nums = []
        curr = ""
        for c in s:
            if c.isnumeric() and curr.isalpha():
                if curr:
                    if strings:
                        strings[-1] += curr
                    else:
                        strings.append(curr)
                curr = c
            elif c == "[":
                nums.append(int(curr))
                strings.append("")
                curr = ""
            elif c == "]":
                if curr != "":
                    if strings:
                        strings[-1] += curr
                    else:
                        strings.append(curr)
                    curr = ""
                decoded = strings.pop() * nums.pop()
                curr = decoded
            else:
                curr += c

            print(c, strings, nums)

        if curr != "":
            strings.append(curr)

        return "".join(strings)

