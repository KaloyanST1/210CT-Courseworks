lis = [2,3,5,7,9,13]
MinX= 10
MaxX = 14 


def BinarySearch(lis, MinX, MaxX):
    x1 = len(lis)                    
    middle = x1//2          
    if x1 == 0:
        return False
    if x1 == 1 and lis[middle] != (MinX or MaxX):
        return False
    if lis[middle] >= MinX and lis[middle] <= MaxX:
        return True
    elif lis[middle] > MaxX:
        return BinarySearch(lis[:middle], MinX, MaxX)
    elif lis[middle] < MinX:
        return BinarySearch(lis[middle:], MinX, MaxX)
    else:
        return False

    

print(BinarySearch(lis, MinX, MaxX,))


#Function(list,Min,Max)
#lenght1 <-lenght(list)
#MiddleOfList <-lenght1 //2
#if lenght1 = 0
#return false
#if lenght1 = 1 and list(MiddleOfList) != Min or Max
#Return false
#if list(MiddleOfList) >= Min and list(MiddleOfList) <= Max
#return True
#else if list(MiddleOfList) > Max
#return Function(list(:MiddleOfList),Min,Max)
#else if list(MiddleOfList) < Max
#return Function(list(MiddleOfList:),Min,Max)
#else
#return false
