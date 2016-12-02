#Function Reversme(string)
#string<-string.split()
#size <- lenght(string)
#index <- size -1
#NumberOfRepeats <- size//2 #now with 100% more "/" so many troubles figuring out that i get an uneven float
#for i <-0 to lenght[A]
#swap =string(index)
#string[index] <- string[i]
#string[i] = swap
#index <- -1 


def ReversTime(strin):      
    strin = strin.split()
    size = len(strin)             
    N = size - 1
    X = size//2                
    for i in range(0, X):    
        swap1 = strin[N]     
        strin[N] = strin[i] 
        strin[i] = swap1
        N -= 1            
        
  
    return strin
strin = "Are you a GoT fan ? Have you played GoT Card game? No? THOUGHT SO !"

print(ReversTime(strin))
 #O(n) - will run as many times as there are words in the string
