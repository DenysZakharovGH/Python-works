#Create a function that takes in 2 numbers and a mathematical function, 
#that also takes 2 numbers as arguments, 
#and then returns the result of the passed argument function given the 2 numbers.   

def cofficient(a,b):
    def add(x):
        def summ():
            return (a+b)*x
        return summ
    return add

print(cofficient(1,5)(2)())