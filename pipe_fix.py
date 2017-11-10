def pipe_fix(arr):
    min = arr[0]
    max = arr[len(arr)-1]
    if min + 1 == max:
        return arr
    else:
        for num in range(0, (max - min)):
            if (arr[num] + 1) != arr[num+1]:
                arr.insert(num+1,arr[num] + 1)
            else:
                pass
        return arr
                
                
pipe_fix([8,9])