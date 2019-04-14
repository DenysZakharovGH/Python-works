#A person class.

#Make a class of called Person. Make the __init__() method take firstname,
#lastname, and age as parameters and add them as attributes. Make another method
#called talk() which makes prints a greeting from the person containing, for
#example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.    

class Person:
    Name ="default"
    LastName ="default"
    Age = 0
    PhoneNumber = "default"
    ItemsList = {}

    # конструктор классу
    def __init__(self,  Name="default" ,LastName="default" ,Age = 0 ,PhoneNumber="default"):
            self.Name = Name
            self.LastName =  LastName
            self.PhoneNumber = PhoneNumber
            self.Age = Age
            self._update_ItemsList()
    
    # Оновимо словник новими значеннями з полів классу  
    def _update_ItemsList(self):
        self.ItemsList ={"Name":self.Name,"LastName":self.LastName,"Age":self.Age,"PhoneNumber":self.PhoneNumber}
    
    # метод для виводу полів классу
    def _get_class_items_(self):
        for k , m in self.ItemsList.items():
            print(" %s : %s" %(k,m))

    # метод для привітання 
    def _do_introduce_(self):
        print(" \tHello, my name - %s %s and I’m %i years old\n \tPhone Number is %s" %(self.ItemsList["Name"],self.ItemsList["LastName"],self.ItemsList["Age"],self.ItemsList["PhoneNumber"]))
       
            
Denys = Person("Denys","Zakharov", 20, "+380668645945")
Denys._get_class_items_()
Denys._do_introduce_()



