import functools
@functools.total_ordering
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    
    def __gt__(self, other: object):
        if not isinstance(other, Person):
            return False
        return self.age > other.age
    
    def greet(self, name="world"):
        
        print(f"Hello, my name is {self.name} and I am {self.age} years old. How are you {name}")
        
p1 = Person("Alice", 30)
p2 = Person("Alice", 40)

print(p1 == p2)
print(p1>p2)
print(p1<p2)
lst = [1,2,3] + [5,6]

print(lst)

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"