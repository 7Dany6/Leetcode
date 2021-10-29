class Solution:
    def myPow(self, x: float, n: int) -> float:
        product, index = 1, abs(n)
        while index:
            if index % 2:
                product *= x
            x *= x
            index //= 2
        return product if n >= 0 else 1 / product
