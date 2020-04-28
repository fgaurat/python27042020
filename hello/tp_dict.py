tel = {'jack': 4098, 'sape': 4139}

for k in tel:
    print(k,tel[k]) 
print(50*'-')
for k,v in tel.items():
    # s = " key : "+str(k)+", value : "+str(v)
    s = " key : {0}, value : {1}".format(k, v)
    print(s) 