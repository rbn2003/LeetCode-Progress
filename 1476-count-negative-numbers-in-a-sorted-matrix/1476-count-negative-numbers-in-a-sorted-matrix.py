class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        countNegatives = 0

        for row in grid:
            for num in row:
                if num < 0:
                    countNegatives += 1
                
        return countNegatives
                    