#realization of divide and conquer sort in python 

import random as rand
import time

unsorted_array = [rand.randrange(0,999) for i in range(10000)]
unsorted_array1 = unsorted_array
unsorted_array2 = unsorted_array


def _merge_sort_(array):
    lens = len(array)
    if lens < 2:
        return array

    l = _merge_sort_(array[: lens // 2])
    r = _merge_sort_(array[lens // 2 : lens])

    i = j = 0
    res =[]
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j +=1
        elif not j < len(r):
            res.append(l[i])
            i +=1
        elif l[i] < r[j]:
            res.append(l[i])
            i +=1
        else:
            res.append(r[j])
            j +=1
    return res

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = int(arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = int(arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10




start_marge_time = time.clock()

_merge_sort_(unsorted_array)

print("marge_time %s seconds ---" % (time.clock() - start_marge_time))


start_sort_time = time.clock()

radixSort(unsorted_array1)

print("radixSort_time %s seconds ---" % (time.clock() - start_sort_time))

start_sort_python_time = time.clock()

unsorted_array2.sort()

print("sort_python time %s seconds ---" % (time.clock() - start_sort_python_time))

