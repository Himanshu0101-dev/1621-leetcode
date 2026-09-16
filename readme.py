MOD = 10**9 + 7

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # Compute nCr modulo MOD
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            num, den = 1, 1
            for i in range(r):
                num = num * (n - i) % MOD
                den = den * (i + 1) % MOD
            # Fermat's little theorem for modular inverse
            return num * pow(den, MOD-2, MOD) % MOD
        
        return nCr(n + k - 1, 2*k)
