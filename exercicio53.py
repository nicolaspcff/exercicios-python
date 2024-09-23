cand1 = 0
cand2 = 0
cand3 = 0
voto  = 0
i = 0
eleitores = int(input("Quantos eleitores votaram? "))
for i in range (i, eleitores):
    voto = int(input("Em quem vc votou? "))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 +=1
    elif voto >= 4:
        print("Voto invalido")
        i = i-1
    else:
        pass

resultado_elei = [(cand1, "candidato 1")], [(cand2, "candidato 2")], [(cand3, "candidato 3")]
print("O vencedor é: ",resultado_elei)
maior=max(resultado_elei)
#print(maior[0])

print(f"O {maior[0][1]} teve {maior[0][0]} votos")
menor= min(resultado_elei)
print(f"O {menor[0][1]} teve {menor[0][0]} votos")