
# solution 1
data = []
value = 10000
while value !=0:
    value = int(input("value : "))
    if value >0:
        data.append(value)

data.sort()
print( data)

# solution 2
data = []
while True:
    value = int(input("value : "))
    if value ==0:
        break
    data.append(value)

l = sorted(data)
print( l)
data.sort()
print( data)


