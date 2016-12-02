#PrimeNumber(X,N)
#x1 = Remainder X ,N
#if M < 1
#Return true
#if x1 =0
#Return False
#PrimeNumber(X,N-1)




def PrimeNumber(X,N):
            Remainder = X % N
            if N <=1:
                print( X ,"Is a prime number")
                return
            if Remainder ==0: #no remainder which means its not prime
                print(X , "Is not a prime number")
                return

            PrimeNumber(X,N-1) #keep calling to see if its prime 
           
x1=int(input("Enter a valid integer: " ))
PrimeNumber(x1,x1-1)
