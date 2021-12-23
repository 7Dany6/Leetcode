class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        top = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}  # storage of top-3 places
        indexes = {val: index for index, val in enumerate(score)}  # storage for initial indexes of elements
        result = [0 for _ in range(len(score))]  # variable for the future answer
        score.sort(reverse=True)

        for index, value in enumerate(
                score):  # we're iterating through all elements in sorted reversed list of initial values
            if index + 1 in top:  # check-up index in "top" dictionary
                result[indexes[value]] = top[index + 1]
            else:
                result[indexes[value]] = str(index + 1)
        return result