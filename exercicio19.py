num1 = input("Digite o primeiro numero: \n")
num2 = input("Digite  o segundo numero: \n")
num3 = input("Digite o terceiro numero: \n")
if (num1>num2 and num2>num3 and num1>num3):
    print (num1, num2, num3)

elif (num2>num1 and num1>num3 and num2>num3):
    print (num2,num1, num3 )

elif (num3>num1 and num2>num3 and num2>num1):
    print (num2,num3,num1)

elif (num1>num3 and num3>num2 and num1>num2):
    print (num1, num3, num2)

elif (num3>num2 and num2>num1 and num3>num1):
    print (num3, num2, num1)

elif (num1>num3 and num3>num2 and num1>num2):
    print(num1, num3, num2)