def sort(my_list):
    i=1
    for j in my_list:
        if j<=my_list[i]:
            if i<len(my_list)-1:
                i+=1
            pass
        else:
            return False
    return True
print(sort([1,1,2,5,7,8,19,89]))
