import random

def ShuffleX(Array):
    Arraylen = len(Array) 
    if Arraylen >2: 
        for x in range(Arraylen): 
            swap = random.randrange(Arraylen - 1) #generate a randomly select
            #ed element from the range
            swap += swap >= x #adds right operand to the left if it is greater
            #than x 
            Array[x], Array[swap] = Array[swap], Array[x]
        return Array
    else:
        print("Array too short")
Array = [1,2,3,5,6,434,11,12,666,888,6969]
print (ShuffleX(Array) )
# O(n ) runtime will increase dependingly of input
#as it needs to go  through all of them to get result
