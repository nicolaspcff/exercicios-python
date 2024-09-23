deposito = int(input("Digite o valor do deposito: "))
juros = input("Digite o valor do juros: ")
juros1 = (juros*deposito)/100
perda = (deposito - juros1)
print ("O valor do seu juros é ", juros1, " E o rendimento total é de ", perda)