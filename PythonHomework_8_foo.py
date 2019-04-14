#Create a simple function called favourite_movie, which takes a string
#containing the name of your favourite movie. The function should then
#print “My favourite movie is name”. 

def favourite_movie(movie):
    print("My favourite movie is %s" % movie)
#favourite_movie("Advanture time")


#Creating a dictionary.

#Create a function called make_country, which takes in a country’s name and
#capital as parameters. Then create a dictionary from those parameters,
#with ‘name’ and ‘capital’ as keys. Make the function print out the values
#of the dictionary to make sure that it works as intended. 

def print_kwargs(country_name,capital):
    CountryDictionary ={country_name:capital}
    for key,val in CountryDictionary.items():
        print (key, "=>", val)


print_kwargs( "USA","Washington")

#A simple calculator.

#Create a function called make_operation, which takes in a simple
#arithmetic operator as a first parameter (to keep things simple let it
#only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only
#numbers) as second parameter. Then return the sum or product of all the
#numbers in the arbitrary parameter. For example:
import operator
def make_operation( sign , a , b):
    ops ={
          "+": operator.add,
          "-": operator.sub,
          "*": operator.mul,
          }
    return ops[sign](a,b)

print(make_operation("*",3,4))