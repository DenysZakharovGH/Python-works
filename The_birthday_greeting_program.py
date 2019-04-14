#The birthday greeting program.

#Write a program that takes your name as input, and then your age as input
#and greets you with the following:

#“Hello <name>, on your next birthday you’ll be <age+1> years”   

UserName = input("Enter your name  :")
UserAge = int(input("Enter your age   :"))
print("Hello {} you will be {} at your next birthday".format(UserName,UserAge+1))