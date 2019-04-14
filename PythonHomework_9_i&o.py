#Saving progress.

#Make a function that takes personal information as arguments, e.g., name,
#last name, phone number, address, etc. Then make another function that
#saves the data onto a file. Make sure that it works by checking that the
#file was created and that it contains the right data. 
#Add to the previous program a function for opening up the same file which the data was saved on. 
#Make sure that it works by making the function print out the data. 

import json

class Person:
    Name ="default"
    LastName ="default"
    PhoneNumber = "default"
    Adress = "default"

    def __init__(self, args):
        self.Name = args[0]
        self.LastName = args[1]
        self.PhoneNumber = args[2]
        self.Adress = args[3]
  

Denys = Person(("Denys","Zakharov", "+380668645945","Kalinina str")) 

def method_name(self):
    return (self.Name,self.LastName,self.PhoneNumber,self.Adress)

with open("data.json","w") as file: #запишимо 
    json.dump(method_name(Denys),file)
#----------------------------------------------------------------------------------------------------------        
with open("data.json") as fileread: #считаємо в ліст
    Denys1 = Person(json.load(fileread))# створимо новий обєкт и передамо в нього значення через конструктор 

# перевіримо 
print(Denys1.PhoneNumber)

fileread.close()
file.close()

