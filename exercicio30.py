num1 = int(input("Digite o primeiro numero: "))
operador = str(input("digite o opreador"))
num2 = int(input("Digite o sgeundo numero: "))
menos= num1-num2
soma= num1+num2
divisao= num1/num2
mult= num1*num2
if operador == '-':
    print(menos)
elif operador == '+':
    print(soma)
elif operador == '/':
    print(divisao)
elif operador == '*':
    print (mult)