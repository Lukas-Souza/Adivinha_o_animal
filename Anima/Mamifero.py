import main
quadrpete = ["Carnivoro", "Herbivoro"]
bipedes = ["onivoro","frutivos"]
mamifero = [ "Quadrupete", "Bipede", "Voador", "Aquatico"]
## mamifero
contador = 0


while contador < len(mamifero):
    main.line()
    print("Esse Animal e um", mamifero[contador])
    re = str(input())

    if re == "s":

        escolha = mamifero[contador]
        contador = 10

    contador+=1
# resolvido 
contador = 0
if escolha == "Quadrupete":

     #  Escolha de Quadrupete

    while contador < len(quadrpete):
        main.line()
        print("Esse animal é um", quadrpete[contador])
        novaresposta = str(input())
        if novaresposta == "s":
            escolha = quadrpete[contador]
            contador = 10
            if escolha == "Carnivoro":
                main.line()
                print("E um leão")
            elif escolha == "Herbivoro":
                main.line()

                print("E um Cavalo")
            else:
                main.line()
                print("nao identificado")
        contador+= 1
    #
# #     # Opçao 2
elif escolha == "Bipede":
    print(bipedes)
    contador = 0
    while contador < len(bipedes):
        main.line()

        print("O animal é", bipedes[contador])
        re = str(input())
        if re == "s":
            novaresposta = bipedes[contador]
            contador = 10
            if novaresposta == "onivoro":
                main.line()

                print("Ele e um Home")
            elif novaresposta == "frutivos":
                main.line()
                print("Ele e um Macaco")
            else:
                main.line()
                print("Animal nao encontrado")
            # termino dos bipedes
        contador+=1


elif escolha == "Voador":
    main.line()
    print("Ele e um Morcego")
elif escolha == "Aquatico":
    main.line()
    print("Ele e uma baleia")    
else:
    print("\033[0;41;mNenhuma das opções selecionadas acima por favor aperte a tecla [F5]")
#____________________________________________-------------------------------------------------------------------__________________________________________-----------------------------------
