my_list=[1,5,9,9,5,3,5,2]
i=0
ii=0
if len(my_list)%2!=0:
    i=len(my_list)+1
    print(i//2)
else:
    i=len(my_list)//2-1
    ii=len(my_list)//2
    sum1=my_list[i]+my_list[ii]
    print(sum1//2)
