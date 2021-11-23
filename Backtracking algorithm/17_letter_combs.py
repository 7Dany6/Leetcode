class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        comb = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        self.combs(digits, '', res, comb, 0)
        return res

    def combs(self, nums, state, res, dic, index):
        if index == len(nums):
            res.append(state)
            return
        string = dic[nums[index]]
        for letter in string:
            self.combs(nums, state + letter, res, dic, index + 1)
