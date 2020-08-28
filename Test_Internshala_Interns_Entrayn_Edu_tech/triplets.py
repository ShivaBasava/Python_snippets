'''
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.If no such triplets can form, print "-1". 

For example: 
Array [1 5 3 2] has 2 Triplets : 1 + 2 = 3 and 3 +2 = 5.

Solution:

This function accepts two parameters-
    List of integer elements and its size
        (Example here,
            myArray = [1, 5, 3, 2] and num = 4
        )
'''

def findTriplet(myArray, num):
    tripletCt = 0  
    myArray.sort()            #Sorting the incoming array in ascending order
    for i in range(num-1, 1, -1):   		
        j = 0      #Initializing all index (i.e, i = num-1, j = 0, k = i-1 )
        k = i - 1             #Each values of i, j, k are compared
        while (j < k): 
            if (myArray[j] + myArray[k] == myArray[i]):
                print('{} + {} = {}'.format(myArray[j],myArray[k],myArray[i]))
                j += 1
                k -= 1
                tripletCt += 1 #Triplet Count is set to 1, 
                                #When a triplet can be formed
            else: 
                if (myArray[j] + myArray[k] < myArray[i]): 
                    j += 1
                else: 
                    k -= 1
    if tripletCt==0:
        return -1   #When there are no triplets can be formed
    return tripletCt


##Program execution starts from here
if __name__ == '__main__': 
    myArray = [1, 5, 3, 2]
    arraySize = myArray.__len__()
    ##If we want dynamic values for 'arraySize' & 'myArray'
    ##we can replace above 2 lines by below
    #arraySize = int(input("Enter the array size followed by its elements:\n"))
    #myArray = [int(input()) for i in range(0,arraySize)]
    print('\nTotal Triplet Count: {}'.format(findTriplet(myArray, arraySize))) 
