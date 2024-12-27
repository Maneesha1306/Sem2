class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.__sal=sal

class Manager(Employee):
    def __init__(self,name,sal,id):
        super().__init__(name,sal)
        self.id=id
    def display(self):
        print(self.name,self._Employee__sal,self.id,sep="\n")#self.__sal=Error(Manager' object has no attribute '_Manager__sal')

m=Manager("Jessa",10000,"6tbb7")    
m.display()