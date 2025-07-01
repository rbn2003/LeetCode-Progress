class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []   #to store all the permutations 

        def backtrack(path, remaining):
            if not remaining:        #if no numbers remain to use 
                result.append(path)   #add the built path to result 
                return 

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i]+ remaining [i+1:])

        backtrack([], nums)
        return result 



