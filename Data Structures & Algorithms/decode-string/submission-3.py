class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        curr = ""
        strings = []
        nums = []
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                strings.append(curr)
                nums.append(int(num) if num != "" else 1)
                num = ""
                curr = ""
            elif char == "]":
                print(strings)
                print(nums)
                curr = strings.pop() + nums.pop() * curr
                print(curr)
            else:
                curr += char

        return "".join(strings) + curr