def insertion_sort(arr):
    for i in range(1,len(arr)):
        c=arr[i]
        for j in range(i,-1,-1):
            if(arr[j]>c):
               arr[i],arr[j]=arr[j],arr[i]
               c=arr[i]
    print(arr)
insertion_sort([300000000,20000,10000,2,20020,3030])

