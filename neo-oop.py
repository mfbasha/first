class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self, name: str = "world") -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old. How are you, {name}?")

    def print_details(self) -> None:
        print(f"{self.name} is a person.")
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id = student_id

def print_person_details(person: Person) -> None:
    if isinstance(person, Person):
        person.print_details()
    else:
        print(f"{person} is not a person.")

# Usage
person_1 = Person("Alice", 30)
person_2 = Person("Bob", 25)

person_1.greet(person_2.name)
person_2.greet(person_1.name)

person_1.name = "Mostafa"
person_1.greet()

print_person_details(person_1)
print_person_details(person_2)
print_person_details("Hello")
    