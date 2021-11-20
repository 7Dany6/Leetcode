class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # here we create a variable for our future resulting list
        self.permute([], res, 0, sorted(nums)) # we call the function described below, giving necessary arguments
        return res # here we return final result , we do this here as we have no 'return' in function permute
    def permute(self, state, result, index, sequence): # the function which implies backtracking algorithm
		result.append(state) # when we get the state, we append it to our result, it takes O(1)
        for num in range(index, len(sequence)): # we are going through all values and after our branch has ended, we return to the value which called this branch, so this is tha main idea of backtracking
            self.permute(state+[sequence[num]], result, num+1, sequence) # after we select a value, we call function again with increased index and updated state
            