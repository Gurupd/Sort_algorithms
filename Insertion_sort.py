# Divide array into sorted and unsorted 
# first value is taken as sorted 



def insertion_sort(arr):
    for index in range(1,len(arr)):
        current_element=arr[index]
        pos=index
        while (current_element<arr[pos-1] and pos>0):
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current_element
    print(arr)

(insertion_sort([6,20,8,2,4]))

# time complexity --O(n^2)