class ProperFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        if self.numerator >= self.denominator:
            whole_part = self.numerator // self.denominator
            numerator = self.numerator % self.denominator
            if numerator == 0:
                return str(whole_part)
            else:
                return f"{whole_part} {numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        result = ProperFraction(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        result = ProperFraction(numerator, denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = ProperFraction(numerator, denominator)
        result.simplify()
        return result

fraction1 = ProperFraction(1, 2)
fraction2 = ProperFraction(3, 4)
fraction3 = ProperFraction(2, 3)

print(fraction1 == fraction2)  # False
print(fraction1 < fraction2)   # True

result = fraction1 + fraction2
print(result)  # 5/4 = 1 + 1/4

result = fraction2 - fraction1
print(result)  # 1/4

result = fraction2 * fraction3
print(result)  # 1/2