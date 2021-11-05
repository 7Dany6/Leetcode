class Solution:
"""
Here we have a typical problem for backtracking algorithm with quite simple solution to understand
"""
    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # we create container for the future result
        self.parenth('', res, n, 0, 0)  # call created function
        return res  # return what we got
    def parenth(self, state, res, n, opening, closing):  # create a function which will store a container, current state, number of opening and closing parentheses
        if len(state) == n * 2:  # as always: think about base case when we return a value(append)
            res.append(state)
        if opening < n:  # if number of opening parentheses is smaller than n, we add 1 opening paranth.
            self.parenth(state+'(', res, n, opening+1, closing)
        if closing < opening:  # we do the same for closing if its number smaller than number of opening
            self.parenth(state+')', res, n, opening, closing+1)
