#Create a function decorator that prints the name of the current running
#function by using the __name__ attribute. Make sure to also decorate some
#different functions to see that it works properly. 

def p_decorate(func):
   print("Function name is : {0}\n".format(func.__name__))
   def func_wrapper(name):
       return func(name)
   return func_wrapper

@p_decorate
def get_text(name):
   return " {0} learn Python".format(name)

print(get_text("John"))
