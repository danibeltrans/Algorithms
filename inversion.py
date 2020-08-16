
import math

count_inversions = 0

def merge (array_left , array_right):
    result = []
    index_left = 0
    index_right = 0
    global count_inversions 

    while index_left < len(array_left) and index_right < len(array_right):
        if array_left[index_left] < array_right[index_right]:
            result.append(array_left[index_left])
            index_left+=1
        else :
            result.append(array_right[index_right])
            index_right+=1
            count_inversions+=len(array_left[index_left:])
    
    return result + array_left[index_left:] + array_right[index_right:]

def mergeSort (array):

    if len(array) == 1:
        return array
    
    middle = math.floor(len(array) / 2)

    array_left = array[:middle]
    array_right = array[middle:]

    return merge(mergeSort(array_left), mergeSort(array_right))



f=open("src/main/resources/input_final.txt", "r")
contents =f.readlines()
int_list = [int(i) for i in contents]
mergeSort(int_list)
print(count_inversions)