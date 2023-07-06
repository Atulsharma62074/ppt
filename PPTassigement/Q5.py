my_list=[1,1,1,2,5,5,32,2,5,2,3,9,6,6,3,4,5]
set1=set(my_list)
my_list=set1
my_list.remove(max(my_list))
print(max(my_list))
