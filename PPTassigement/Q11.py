my_list1=[1,65,4,8,4,56,6,41,3,6,54,1]
my_list2=[5,2,6,9,7,4,5,6,4,2,6,54,8,41]
my_comlist=[]
for i in set(my_list1):
    for j in set(my_list2):
        if i==j:
            my_comlist.append(i)
print(my_comlist)
            
a=[2,9,4,5]
b=[3,5,7,9]
def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))
e=common(a,b)
print(e)
