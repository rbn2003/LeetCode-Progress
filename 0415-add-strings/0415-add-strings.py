class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)

        sum_result = num1 + num2
        sum_as_string = str(sum_result)
        return sum_as_string

        