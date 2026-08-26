class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        heights.append(0)

        for h in heights:
            length = 1 
            while stack and stack[-1][0] > h:
                last_height, last_length = stack.pop()
                max_area = max(max_area, last_height * (last_length + length - 1))
                length += last_length 
            stack.append((h, length))

        return max_area

            
