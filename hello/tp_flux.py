words = ['cat', 'window', 'defenestrate']
dest=[]
for w in words:    
    if len(w)<12:
        dest.append(w)
    print(w, len(w))

print(words)
print(dest)

for i in range(len(words)):
    print(i,words[i])

r = range(4)
print(r)
l = list(r)
print(l)

for i in range(0,5):
    if i ==3:
        pass
    print(i)