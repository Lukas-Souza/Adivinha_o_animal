
aves = ["Não Voadores", "Nadadoras", "De rapina"]
Nao_voadores = ["Tropicais", "Polares"]
contador = 0
#  Declaração de Variaveis
#  Pergunta sobre que tipo de ave ele é
while contador < len(aves):
    print("O Animal é", aves[contador],":")
    re = str(input())
    if re == "s":
        res = aves[contador]
        contador = 10
    contador+= 1
# Classificaçao da ave 

if res == "Não Voadores":
    # Perguntando que tipo de nao voadores ele e
    contador = 0
    while contador < len(Nao_voadores):
        print("Esse animal é um", Nao_voadores[contador],":")
        re = str(input())
        if re == "s":
                resresn = Nao_voadores[contador]
                contador = 10
        contador +=1

elif  res ==  "Tropicais":
        print("Ele é um avestruz")

elif  res == "Polares":
        print("Ele é um piguin")
elif  res == "Nadadoras":
        print("Ele é um Pato")  
else:
        print("Não encontrado")

