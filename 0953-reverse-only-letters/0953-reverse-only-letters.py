class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        # Initialize two pointers
        left, right = 0, len(s_list) - 1

        while left < right:
            # Move left pointer if it's not pointing to a letter
            if not s_list[left].isalpha():
                left += 1
            # Move right pointer if it's not pointing to a letter
            elif not s_list[right].isalpha():
                right -= 1
            else:
                # Swap the letters
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        # Convert the list back to a string
        return ''.join(s_list)