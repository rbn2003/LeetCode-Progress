class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = Counter(s)  # Count occurrences of each character
        length = 0
        has_odd = False

        for count in char_count.values():
            if count % 2 == 0:
                length += count  # Add even counts completely
            else:
                length += count - 1  # Add even part of odd counts
                has_odd = True  # Mark that we have an odd count

        return length + 1 if has_odd else length  # Add 1 if an odd character can be placed in the middle

