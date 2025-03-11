#1
def longest_common_prefix(strings):
    if not strings:
        return ""
    
    # Sort the tuple of strings
    sorted_strings = sorted(strings)
    
    # Compare first and last string
    first = sorted_strings[0]
    last = sorted_strings[-1]
    
    prefix = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix.append(first[i])
        else:
            break
    
    return "".join(prefix)
strings = ("Flower", "Flow", "Flight")
print(longest_common_prefix(strings))  

#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)  
        self.student_id = student_id
        self.course = course
    def display_info(self):
        super().display_info()  
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

person1 = Person("Alice", 30)
student1 = Student("Bob", 20, "S12345", "Computer Science")
print("Person Details:")
person1.display_info()
print("\nStudent Details:")
student1.display_info()

