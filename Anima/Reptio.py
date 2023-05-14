import main
reptio = ["Com Casco", "Carnivoro", "Sem patas"]
contador = 0
while contador < len(reptio):
    main.line()    
    print("Esse Reptio e um", reptio[contador])
    res =str(input())
    if res == "s":
        respo = reptio[contador]
        contador = 10
    contador+=1

if respo == "Com Casco":
    main.line()   
    print("E uma Tartaruga")
elif respo == "Carnivoro":
    main.line()    
    print("E um crocodilo")
elif respo == "Sem patas":
    main.line()    
    print("E uma Cobra")