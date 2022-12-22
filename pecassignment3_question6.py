
repeat = "Y"
dictionary1 = {}
dictionary2 = {}
# Y or N
liste = ["Y", "y", "n", "N"]
while repeat == "Y" or repeat == "y":

    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid < 0:
        print("\nError\nSID can't be negative\n")
    else:

        dictionary1.update({sid: name})

        dictionary2.update({name: sid})

        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat == "N" or repeat == "n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat = str(input("\nEnter Y to continue or N to end:"))

# a
# printing the dictionary

print("The Dictionary containing {'SID':'Name'} is shown below")
print(dictionary1)
# b
# sorting according to name

list_k = sorted(dictionary2)
dictionary3 = {}
for ele in list_k:
    dictionary3.update({dictionary2.get(ele): ele})
print("The Dictionary after sorting according to name:")
print(dictionary3)

# c
# sorting according to SID

sort_dic = sorted(dictionary1)
dictionary4 = {}
for va in sort_dic:
    dictionary4.update({va: dictionary1.get(va)})
print("The Dictionary after sorting according to SID:")
print(dictionary4)
# d
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dictionary1.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")