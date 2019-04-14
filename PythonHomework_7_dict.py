#dict comprehension exercise.

#Make a program that given a whole sentence (a string) will make a dict
#containing all unique words as keys and the number of occurrences as
#values. 

Sentances = "Make a program that given a whole sentence (a string) will make a dict containing all unique words as keys and the number of occurrences as values"
listWords=Sentances.split()# розбиваем строку поелементно в масив
dict = { listWords[i] : Sentances.count(listWords[i])  for i in range(0,len(listWords))} # магия питона
print(dict)
    

#containing all unique words as keys and the number of occurrences as
#values"
#List comprehension exercise I.

#Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Now, make a program (no longer than one line) that makes a new list
#containing all the values in a
#but no even numbers. 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
listNotEven = [i for i in a if i % 2!=0]

#List comprehension exercise II.

#Use a list comprehension to make a list containing tuples (i, j) where i
#goes from 1 to 10 and j is corresponding i squared. .  
tupleOfSquared =[(i,i**2) for i in range(10)]
print(tupleOfSquared)