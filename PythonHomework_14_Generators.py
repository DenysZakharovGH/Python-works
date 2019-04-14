#Create a generator function that yields all squares of integers
#within a given range, i.e., arguments start and stop.  

def _squares_generators_(start,stop):
    i = start
    for i in range(stop):
        yield i**2

a = _squares_generators_(1,10)

result_list = []

i =0
while i<10:
    result_list.append(next(a))
    i +=1

print( result_list)