class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return heights[0]
        stack = [] # (index, height)
        max_area = 0
            
        for i, height in enumerate(heights):
            if i > 0 and height == heights[i-1]:
                stack[-1] = (i, height)
                
            while stack and height < stack[-1][1]:
                _, curr_height = stack.pop()
                
                right = i
                left = -1
                if stack:
                    left = stack[-1][0]
                    
                width = right - left - 1
                curr_area = curr_height * width
                max_area = max(max_area, curr_area)

            stack.append((i, height))
        
        while stack:
            _, curr_height = stack.pop()
            
            right = len(heights)
            left = -1
            if stack:
                left = stack[-1][0]
            
            width = right - left - 1
            curr_area = curr_height * width
            max_area = max(max_area, curr_area)
            
        
        return max_area