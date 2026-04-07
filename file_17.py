class MathUtils:
    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n-1)
