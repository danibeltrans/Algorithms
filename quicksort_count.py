import math
count_comparation = 0

def quickSort (array, low, high):
    if low >= high:
        return array
    
    global count_comparation

    i = choose_pivot(array, low, high)
    array[low],array[i] = array[i],array[low]
    j=partition(array, low, high)

    quickSort(array, low, j-1)
    count_comparation+= (j)-low


    quickSort(array, j+1, high)
    count_comparation += high-(j)
   

def choose_pivot(array, low, high):
    #return low
    return high
    
    """middle = array[math.floor((high+low)/2)]

    first = array[low]
    last = array[high]

    median = [middle, first, last]
    median.sort()

    if median[1] == middle:
        return math.floor((high+low)/2)
    if median[1] == first:
        return low
    if median[1] == last:
        return high"""
    

    

def partition(array, low, high):
    p=array[low]
    i=low+1

    for j in range (low+1, high+1):
        if array[j] < p:
            array[j],array[i] = array[i], array[j]
            i = i + 1
        
    array[low],array[i-1] = array[i-1], array[low]
    return i-1

def partition2(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

f=open("src/main/resources/input_QuickSort.txt", "r")
contents =f.readlines()
int_list = [int(i) for i in contents]

#print(int_list)
quickSort(int_list, 0, len(int_list)-1)
#print(int_list)
print(count_comparation)