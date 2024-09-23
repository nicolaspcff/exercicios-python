import math
area = float(input("Digite a area a ser pintada: "))
tinta=18
preco=80
quant_lata = math.ceil(area/tinta)
precototal= quant_lata*preco
print(quant_lata)
print("A quantidade que você vai ter que comprar é de ", quant_lata, "e o preco a pagar vai ser ", precototal)