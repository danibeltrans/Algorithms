
import math

def merge (array_left , array_right):
   print('array_left : ' ,  array_left, ' array_rigth : ' , array_right) 
   result = []
   index_left = 0
   index_right = 0

   while index_left < len(array_left) and index_right < len(array_right):
        if array_left[index_left] < array_right[index_right]:
            result.append(array_left[index_left])
            index_left+=1
        else :
            result.append(array_right[index_right])
            index_right+=1
            
        
    
   return result + array_left[index_left:] + array_right[index_right:]

def mergeSort (array):

    if len(array) == 1:
        return array
    
    middle = math.floor(len(array) / 2)

    array_left = array[:middle]
    array_right = array[middle:]

    return merge(mergeSort(array_left), mergeSort(array_right))



array = [5, 3, 8, 9, 1, 7, 0, 2, 6, 4]
print(mergeSort(array))