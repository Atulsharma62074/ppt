list1=[1,1,2,5,7,8,19,89]
list2=[1,5,4,8,9,5,42,2,19]
comman=[]

for i in list1:
    for j in list2:
        if i==j:
            comman.append(i)
print(list(set(comman)))
