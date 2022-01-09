arr = [1,4,8,3,6]

def bubble(arr,r,c):
    if r==0:
        return
    
    if c<r:
        if arr[c]>arr[c+1]:
            temp = arr[c]
            arr[c] = arr[c+1]
            arr[c+1] = temp
            
        bubble(arr,r,c+1)
        
    else:
        bubble(arr,r-1,0)
    
bubble(arr, (len(arr)-1),0)
print(arr)
    