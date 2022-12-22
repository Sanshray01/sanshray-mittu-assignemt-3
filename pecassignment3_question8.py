set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

# a.
union = set1.union(set2)
intersection = set1.intersection(set2)
set_a = set()
for i in union:
    if i not in intersection:
        set_a.add(i)
print(set_a)

# b.
set_b = set()
intersection2 = set2.intersection(set3)
intersection3 = set1.intersection(set3)
v = intersection.union(intersection2)
v = v.union(intersection3)
u = union.union(set3)
for j in u:
    if j not in v:
        set_b.add(j)
print(set_b)

# c.
set_c = set()
w = intersection.intersection(intersection2)
for k in v:
    if k not in w:
        set_c.add(k)
print(set_c)

# d.
set_d = set()
for l in range(1, 11):
    if l not in set1:
        set_d.add(l)
print(set_d)

# e.
set_e = set()
for m in range(1, 11):
    if m not in u:
        set_e.add(m)
print(set_e)