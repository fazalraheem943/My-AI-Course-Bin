customerlist=["fazal",222,234.5,True]

print(customerlist)

print(type(customerlist))

customerlist.append("lahore")

customerlist.insert(1,"ping")

print(customerlist)

print(customerlist[1])

print(type(customerlist[1]))

customerlist.remove(222)

print(customerlist)

customerlist.pop(1)

print(customerlist)

customerlist[0]="my changed value"
print(customerlist)