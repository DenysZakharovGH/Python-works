import random
#1/ Exclusive common numbers.

#Generate 2 lists of length 10 with random integers from 1 to 10, and make
#a third list containing the common integers between the 2 initial lists
#without any duplicates. 
FirstList = [random.randint(1, 10) for i in range(10)]

SecondList =[random.randint(1, 10) for i in range(10)]

LastSet = {} 
LastSet = set(FirstList) & set(SecondList)

print (LastSet)

#2/ Extracting numbers.

#Make a list that contains all integers from 1 to 100, then find all
#integers from the list that are divisible by 7 but not a multiple of 5 and
#store them in a separate list. Finally print the list.  

InputList = [item for item in range(100)]
OutputList = [item for item in InputList if item % 7==0 if item % 5!=0]
print (OutputList)

