for i in range(11):
    for j in range(11):
      print(i,"x",j,"=",i*j)

# Lo mismo, de otro modo
for i in range(11):
    for j in range(11):
      print(" %d x %d = %d" % (i, j, i*j))
