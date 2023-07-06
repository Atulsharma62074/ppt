number=int(input("Enput a number"))
a,b,s=-1,1,0
while number>0:
    a,b=b,a+b
    print(b)
    number-=1
    
