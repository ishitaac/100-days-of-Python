num = int(input("Enter the number: "))
flag = False
i=2

while i<= num/2:
    if(num%i==0):
        flag = True
        break
    else:
        i=i+1

if flag == True:
    print("Not Prime number")
else:
    print("Prime Number")