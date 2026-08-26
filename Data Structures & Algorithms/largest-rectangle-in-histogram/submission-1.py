class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for height in heights:
            length = 1
            while stack and stack[-1][0] > height:
                last_height, last_length = stack.pop()
                max_area = max(max_area, last_height * (last_length + length - 1))
                length += last_length 
            stack.append((height, length))

        return max_area