num = int(input("Digite o número "))
if num>1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "n e primo")
            break
        else:
            print(num, " é primo")
elif num==0:
    print(num, "é zero")
else:
    print(num,"é negativo")




 