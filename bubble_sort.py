def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)

# Time complexity -- O(n^2)


print(bubble_sort([4,-2,8,9,5]))