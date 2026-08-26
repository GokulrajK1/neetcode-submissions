class Solution:
    def decodeString(self, s: str) -> str:
        strings = []
        nums = []
        curr = ""
        num = ""

        for c in s:
            if c.isdigit():
                num += c
            elif c == "[":
                strings.append(curr)
                nums.append(1 if num == "" else int(num))
                curr = ""
                num = ""
            elif c == "]":
                curr = strings.pop() + nums.pop() * curr
            else:
                curr += c 

        if curr != "":
            strings.append(curr)

        return "".join(strings)