class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1 
            else:
                counts[num] = 1
        for num, counts in counts.items():
            if counts > len(nums) //2 :
                return num

        return None 
        