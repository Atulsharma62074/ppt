dpl = [1,1,2,1,3,4,1,2,3,4]
ddl = list()

for item in dpl:
    if item not in ddl:
        ddl.append(item)

print(ddl)
