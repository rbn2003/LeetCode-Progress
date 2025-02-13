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

        ## return s.reverse()  
        
        left = 0
        right = len(s) -1 
        while left < right:
            s[left] , s[right] = s[right] , s[left]
            left += 1
            right -= 1
        return 