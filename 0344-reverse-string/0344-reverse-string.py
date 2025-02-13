class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        """m = len(s)
        result  = []


        for i in range (m - 1, -1, -1):
            result.append(s[i])

        for i in range(m):
            s[i] = result[i]

        print(s)"""

        return s.reverse()  
        