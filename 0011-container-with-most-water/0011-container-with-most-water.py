class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0           #starting pointer 
        right = len(height)-1        #ending pointer
        max_water = 0  #storage of water 


        while left<right:
            h = min(height[left], height[right])
            w = right - left
            current_area = h*w
            max_water = max(max_water, current_area)

        #moving the pointer towards the shorter end 
            if height[left] < height[right]:
                left += 1 
            else:
                right -=1 

        return max_water