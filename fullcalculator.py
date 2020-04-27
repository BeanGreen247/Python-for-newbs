ex = 0

x = input("Enter the first number:")
y = input("Enter the second number:")
num = int(x)
num1 = int(y)

while ex!=1:
    a = input("Pick an operation"+"\n0-New Numbers"+"\n1-Sum"+"\n2-Sub"+"\n3-Mul"+"\n4-Div"+"\n5-Exit"+"\nYour pick:")
    sw = int(a)
    
    if sw == 0:
       x = input("Enter the first number:")
       y = input("Enter the second number:")
       num = int(x)
       num1 = int(y)
    elif sw == 1:
        res = num+num1
        print(str(num)+"+"+str(num1)+"="+str(res))
    elif sw == 2:
        res = num-num1
        print(str(num)+"-"+str(num1)+"="+str(res))
    elif sw == 3:
        res = num*num1
        print(str(num)+"*"+str(num1)+"="+str(res))
    elif sw == 4:
        res = num/num1
        print(str(num)+"/"+str(num1)+"="+str(res))
    elif sw == 5:
        ex=1
    else:
        print("No operation selected...")