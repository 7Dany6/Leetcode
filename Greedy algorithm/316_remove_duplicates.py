class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = {el: index for index, el in enumerate(s)}  # write down last indexes for the values
        result = [s[0]]  # variable for future result

        for i in range(1, len(s)):  # start from index 1 as the first value has already been added
            if s[i] in set(
                    result):  # remember: looking for a value in a set takes O(1) instead of O(n) in array, that's why it's much better to transform your list to a hash table
                continue
            while result[-1] > s[i] and seen[result[-1]] > i:
                result.pop()
                if len(result) == 0:
                    break
            result.append(s[i])
        return ''.join(result)
