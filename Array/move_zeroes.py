class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for el in nums:
            if el == 0:
                nums.append(0)
                nums.remove(el)
