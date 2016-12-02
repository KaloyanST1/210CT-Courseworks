
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def TrailingZeros(N):
    X = str(N)
    return len(X)-len(X.rstrip('0'))

n=int(input("please enter an integer"))
print("The number of trailing zeros are : " ,TrailingZeros(factorial(n)),
      "And your factorial of the number is: " ,factorial(n))
# O(n) program won't slow down with increased problem (n) 
