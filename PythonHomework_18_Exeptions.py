#Write a function that takes in two numbers from the user via input(),
#call the numbers a and b, and then returns the value of a squared divided by b,
#construct a try-except block which
#raises an exception if the two values given by the input function were not numbers, 
#and if value b was zero (cannot divide by zero).   
 
while 1 :
    try:
        a = float(input("Input a :"))
        b = float(input("Input b :"))
        try:
            print((a/b)**2)
            break
        except ZeroDivisionError as arr:
            print(arr)
    except ValueError as arr:
        print(arr,)

