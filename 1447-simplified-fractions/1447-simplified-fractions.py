class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        return [f"{i}/{j}" for j in range(2, n + 1) for i in range(1, j) if gcd(i, j) == 1]