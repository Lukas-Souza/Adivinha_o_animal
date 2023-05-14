import os
def line():
    os.system('cls')
    print("\033[1;31;43m##################################################################################################################")
    print("\033[1;31;34m                                  Adivinho o seu o seu pensamento                                                 \033[m")
    print("\033[1;31;43m##################################################################################################################\033[m")

# Inicio do programa 
line()
animal = ["Ave", "Mamifero", "Reptio"]
maincontador = 0
while maincontador < len(animal):
    line()
    print("Esse Animal e um", animal[maincontador],":")
    mainrespota = str(input())
    if mainrespota == "s":
        seleanimal = animal[maincontador]
        maincontador = 10
    
    maincontador+=1
print
if seleanimal == "Ave":
    import Aves
    
elif seleanimal ==  "Mamifero":
    import Mamifero
    
elif seleanimal == "Reptio":
    import Reptio
    
else:
    print("Aperte [F5] para recarregar")