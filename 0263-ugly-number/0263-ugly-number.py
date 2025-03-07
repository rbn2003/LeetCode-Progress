class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
    
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor  # Keep dividing by the factor
            
        return n == 1  # If we are left with 1, it's an ugly number
        