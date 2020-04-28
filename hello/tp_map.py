
def mult2(value):
    return value*2


l = [12,48,98]
ll = list(map(mult2,l))
ll2 = list(map(lambda v: v*2,l))
ll3 = [v*2 for v in l]
print(ll)
print(ll2)
print(ll3)