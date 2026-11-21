def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)


n=int(input("enter a number:"))
factorial(n)
print("the answer is :",factorial(n))
# print(f"the factorial of this  no. is: {factorial(n)}")
