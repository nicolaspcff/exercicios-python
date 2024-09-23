anoA=2024

anonasc = int(input("Digite o ano do seu nascimento "))
anos = anoA-anonasc
mes = int(input("Digite o mes do seu nascimento(em numero) "))
meses = (12*anos) + mes
semanas = anos*52
dia = int(input("Digite o dia do seu nascimento"))
dias = anos*365

print("Sua idade em anos é: \n", anos)
print("Sua idade em meses é: \n", meses)
print("Sua idade em semanas é: ", semanas),
print("Sua idade em dias é: ", dias)