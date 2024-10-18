class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, name="world"):
        
        print(f"Hello, my name is {self.name} and I am {self.age} years old. How are you {name}")
    def __format__(self, format_spec: str) -> str:
        return f"Person(name={self.name}, age={self.age})"
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
person_1 = Person("Alice", 30)

person_2 = Person("Bob", 25)
person_1.greet(person_2.name)
person_2.greet(person_1.name)

person_1.name = "Mostafa"
person_1.greet()

def print_person_details(person):
    if isinstance(person, Person):
        print(f"{person.name} is a person.")
        print(f"Name: {person.name}, Age: {person.age}")
    else:
        print(f"{person} is not a person.")
print_person_details(person_1)
print_person_details(person_2)
print_person_details("Hello")