arr=[0,1,1,0,1,2,1,2,0,0,0,1]
n=len(arr)
#sort array of 0,1,2

def func1(arr, n):
    low=0
    mid=0
    high=n-1
    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)