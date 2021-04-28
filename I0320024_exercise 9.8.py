import array
#mengonversi list ke dalam array.array
li = [10, 20, 30, 40, 50]
c = array.array("i")
c.fromlist(li)
type(c)
for nilai in c:
	print("%d " % nilai, end=" ")