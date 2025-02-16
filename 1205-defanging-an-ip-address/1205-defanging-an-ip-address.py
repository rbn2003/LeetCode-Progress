class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        result = []
        for i in address:
            if i == '.' :
                result.append('[.]')
            else:
                result.append(i)
        return ''.join(result)
