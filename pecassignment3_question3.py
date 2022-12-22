# making a lsit of tuples.
list_num  = int(input('enter numbetr of terms you want in your list : '))
t = []
for i in range(0,list_num):
    items = int(input(f"enter {i+1}th item of list : "))
    t.append(items)
t.sort()
y = []
for j in range(0,list_num):
    g = t[j]**2
    y.append(g)

list_tuples = list(zip(t,y))
print(list_tuples)


