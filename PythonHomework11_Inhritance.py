#Make a class structure in python representing people in a school. 
#Make a base class called Person, a class called Student, and another one called Teacher. 
#Try to find as many methods and attributes as you can which belong to the different classes, 
#and keep in mind which are common and which are not. For example name should be a Person attribute,
#while salary should only be available to Teacher.  

class Person:
   
    def __init__(self,Name,
                    Sex,
                    Age,
                    UniversityName,
                    Faculty,):
        self.Name = Name
        self.Sex =  Sex
        self.Age = Age
        self.UniversityName = UniversityName
        self.Faculty = Faculty

        def __str__ (self):
            return self.Name,self.Sex,self.Age,self.UniversityName,self.Faculty 


class Teather(Person):
    def __init__(self,Name,
                    Sex,
                    Age,
                    UniversityName,
                    Faculty, 
                    Experience, 
                    Salary,
                    Subject):
        super().__init__(Name,Sex,Age,UniversityName,Faculty)
        self.Experience = Experience
        self.Salary = Salary
        self.Subject = Subject

    def _Teach__(self, others):
        others. __Stady__(self)

    def __str__ (self):
            return self.Name,self.Sex,self.Age,self.UniversityName,self.Faculty,self.Experience,self.Salary,self.Subject


class Student(Person):
    def __init__(self,Name,
                    Sex,
                    Age,
                    UniversityName,
                    Faculty,
                    Course, # year of education
                    Group, # group name
                    Grand,): # scholarship):
        super().__init__(Name,Sex,Age,UniversityName,Faculty)
        self.Course = Course
        self.Group =  Group
        self.Grand = Grand


    def __Stady__(self,other):
        print("My name is - %s and I'm tought by %s \n" %(self.Name ,other.Name))

    def __str__ (self):
            return [self.Name, self.Sex, self.Age, self.UniversityName, self.Faculty, self. Course, self.Group, self.Grand]

class _str_:
    def __init__(self,other):
        print(str(other.__str__()))
    
        


Vancho = Student("Vancho", "M", 21, "PNTY","Computer Ingeniring",3,"301-TK",3100 )
Petrovich = Teather("Petrovich", "M", 56, "PNTY","Computer Ingeniring",20,7800,"C++")
_str_(Vancho)
_str_(Petrovich)

Petrovich._Teach__(Vancho)