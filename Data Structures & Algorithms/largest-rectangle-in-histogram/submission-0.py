class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for height in heights:
            length = 1 
            while stack and stack[-1][0] >= height:
                last_height, last_length = stack.pop()
                print("Last Stuff: {last_height}, {last_length}")
                print(f"Area: {last_height * (last_length + length - 1)}")
                max_area = max(max_area, last_height * (last_length + length - 1))
                length += last_length 
                print(f"Length: {length}")
            stack.append([height, length])
            print(f"Stack {stack}")

        return max_area

