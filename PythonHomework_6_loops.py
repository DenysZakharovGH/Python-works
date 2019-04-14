#1
#Make a program that generates a list that has all squared values of integers
#from 1 to 100, i.e., like this: [1, 4, 9, 16, 25, 36, …, 10000] 

Squaredlist = [x**2 for x in range(100)]
print(Squaredlist)

#2
#Make a program that prompts the user to input the name of a car, the program
#should save the input in a list and ask for another, and then another,
#until the user inputs ‘q’, then the program should stop and the list of
#cars that was produced should be printed. 
UserCarsList=[]
while True:
    UserCarsList.append(input("Write a new car there :"))
    if input("press q for exit") == 'q': break

for i in UserCarsList:
    print(i,end=" ")


#3
#Start of with any list containing at least 10 elements, then print all elements
#in reverse order. 

CusualList = ["Table", "Chairs", 10, 3.1415926, 0x0010,  "Soft", 228,  'q',UserCarsList[0],UserCarsList ]
print(CusualList)
ReverseList =CusualList[::-1] 
print(ReverseList)