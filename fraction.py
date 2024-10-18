import functools
@functools.total_ordering
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator  
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    def __add__(self, other: object) -> object:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for +")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: object) -> object:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for -")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: object) -> object:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for *")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for >")
        return self.numerator * other.denominator > other.numerator * self.denominator
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for <")
        return self.numerator * other.denominator < other.numerator * self.denominator
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for ==")
        return self.numerator * other.denominator == other.numerator * self.denominator
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for >=")
        return self.numerator * other.denominator >= other.numerator * self.denominator
    def __le__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for <=")
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 > f2)
print(f1 < f2)
print(f1 == f2)