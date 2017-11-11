
#! /bin/python
# This algo shifts the given array N times. Looking at this now I feel it could probably be much more efficient. 
import sys
a = [1,2,3,4,5]
d = 4

def leftRotation(a, d):
    for x in range(d):
        #store 0 element in temp variable.
        temp = a[0]
        #loop through array replacing each element with value to the right.
        for number in range(len(a) - 1):
            a[number] = a[number + 1]
        #once the loop finishes set final element to the stored variable. 
        a[len(a) - 1] = temp
        print (a, sep=' ')
    
leftRotation(a,d)

#should result 
# [5 1 2 3 4]
