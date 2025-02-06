class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = [] #using a list to store scores. 

        for op in operations:
            if op =="C":
                if scores:
                    scores.pop() #remove the last valid scores
            elif op =="D":
                if scores:
                    scores.append(2*scores[-1]) #double the last score
            elif op =="+":
                if len(scores) >= 2: 
                    scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(op))

        return sum(scores)
            