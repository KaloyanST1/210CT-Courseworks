def BubbleSort(lis):


    for x in range(len(lis)-1,0,-1):
        for i in range(x):
            if lis[i] >=lis[i-1]:
                temp = lis[i]
                lis[i] = lis[i-1]
                lis[i-1] = temp

lis = [54,26,93,17,77,31,44,55,20]
BubbleSort(lis)
print(lis)


#Why is the max el. at the end ? i Don't know either , its either i'm blind
#and i can't see my error or theres none
