def binary(number):
  if number/2:
         binary(number//2)
  print(number%2,end="")

binary(135)
