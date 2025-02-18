class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_num = 0
        sign = -1 if x < 0 else 1  # Store the sign of the number
        x = abs(x)  # Work with the absolute value

        while x != 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x = x // 10

        rev_num *= sign  # Restore the sign

        # Handle 32-bit integer overflow
        if rev_num < -2**31 or rev_num > 2**31 - 1:
            return 0

        return rev_num
