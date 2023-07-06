def numisprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return "Not Prime"
    return "Prime"
print(numisprime(int(input("Enter a number"))))
