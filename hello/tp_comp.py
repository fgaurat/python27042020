def func(*p):
    print(p)
    print(p[0])
    print(p[1])
    print(p[2])

l1 = [x*10 for x in range(5)]


l2 = [x*10 for x in range(5,10)]


l = [l1, l2,"toto"]

if "toto" in l:
    print("toto in l")

# print(list(zip(l1,l2)))
# print(list(zip(*l)))


# for i1 in range(len(l)):
#     for i2 in range(len(l[i1])):
#         print("["+str(i1)+"]["+str(i2)+"] "+str(l[i1][i2]))


# for i1,v in enumerate(l):
#     for i2,v2 in enumerate(v):
#                 print("["+str(i1)+"]["+str(i2)+"] "+str(v2))



# """
# [0][0] 0
# [0][1] 1
# [0][2] 2
# [0][3] 3
# [0][4] 4
# [1][0] 5
# [1][1] 6
# """