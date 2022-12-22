# finding sum of fibbonacci sequence and average of the same.
num1 = int(input("tell the number upto you want the sum and average of the fibbonacci sequence : " ))
fibbonacci=[0,1]
sum_ = 0
for i in range(0,int(num1)+1):
    if i>=2:
        fibbonacci.append(fibbonacci[i-1] + fibbonacci[i-2])
print(fibbonacci[i],end="\t")
sum_ = int(fibbonacci[i])
if i ==int(num1):
    print(f"\n the average of the numbers of fibbonacci sequence is = {sum_/(int(num1+1))}")

