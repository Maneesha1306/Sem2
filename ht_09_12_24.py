#1
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"Photo is taken with {self.resolution} resolution")


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self):
        print(f"Calling from the number {self.phone_number}.")

    def send_message(self,message):
        print(f"Sending message from {self.phone_number} as: {message}")


class Smartphone(Camera, Phone):
    def __init__(self, resolution, phone_number, brand, model):
        Camera.__init__(self, resolution)
        Phone.__init__(self, phone_number)
        self.brand = brand
        self.model = model

    def display_device_information(self):
        print (f"Smartphone Information:\nBrand: {self.brand}\nModel: {self.model}\nResolution: {self.resolution}\nPhone Number: {self.phone_number}")


s = Smartphone("108MP",8975435643,"Samsung","Galaxy ZFlip")

s.take_photo()
s.make_call()
s.send_message("Hello!")
s.display_device_information()

#2
class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def studentInfo(self):
        print(f"Name:{self.name}\nCourse:{self.course}")
class StudentAthlete(Student):
    def __init__(self,name,course,sport_name):
        super().__init__(name,course)
        self.sport_name=sport_name
    def displayAthlete(self):
        self.studentInfo()
        print("Sport Name:",self.sport_name)

stud=StudentAthlete("Abi","BSc CS","Basketball")
stud.displayAthlete()
