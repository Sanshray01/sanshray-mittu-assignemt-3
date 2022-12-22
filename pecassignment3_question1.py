#finding the occurance of words and letters.
line = input("enter your text here :")
length = len(line)
y = ' '.join(line.split())
length2= len(y)
unique = []
if " " not in y:
    for i in range(0,length2):
        occurance = f"The number of occurance of {y[i]} is {y.count(y[i])}"
        if occurance in unique:
            continue
        else:
            unique.append(occurance)

    for item in unique:
        print(item)


else:
    x = line.split()
    length3 = len(x)
    for j in range(0,length3):
        occurance2 = f"the number of occurance of {x[j]} is {x.count(x[j])}"

        if occurance2 in unique:
            continue
        else:
            unique.append(occurance2)
    for items in unique:
        print(items)