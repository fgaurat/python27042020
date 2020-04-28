data = []
value = 10000
while value !=0:
    value = int(input("value : "))
    if value>0:
        data.append(value)

print(50*'-')
for d in data:
    print(d,end=", ")
print()
print(50*'-')

for i in range(-1,-len(data)-1,-1):
    print(data[i])

print(50*'-')

while len(data)>0:
    print(data.pop(),end=", ")
print()    