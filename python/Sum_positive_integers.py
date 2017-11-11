# super simple kata from codewars. I debated if this was even worth uploading.

def positive_sum(arr):
    sum = 0
    if len(arr) == 0:
        return 0
    else:
        for num in arr:
            if num > 0:
                sum += num
    return sum
