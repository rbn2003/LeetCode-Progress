class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = set()

        for i in nums:
            if (i) in result:
                return True
            result.add(i)


        return False
