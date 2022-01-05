kw = int(input("Qual a quantidade de KW consumida?: "))
print ("Informe o tipo de instalação")
print("Aperte [R] para Residencial")
print("Aperte [C] para Comercial")
print("Aperte [I] para Industrial")
print("Aperte [X] para SAIR")
tipo = str(input(":"))
if (tipo == "R" or tipo == "r"):
    print("Sua instalação é do tipo Residencial")
    aci = kw - 500 
    if (aci <= 0):
        preco = kw * 0.40
        print("Gastos de energia com base nos KW",preco)
    else:
        preco = kw * 0.65
        print("Gostos com energia com base no consumo acima do limite",preco)
elif (tipo == "C" or tipo == "c"):
    print("Sua instalação é do tipo Comercial")
    aci = kw - 1000 
    if (aci <= 0):
        preco = kw * 0.55
        print("Gastos de energia com base nos KW",preco)
    else:
        preco = kw * 0.60
        print("Gostos com energia com base no consumo acima do limite",preco)
elif (tipo == "I" or tipo == "i"):
    print("Sua instalação é do tipo Industrial")
    aci = kw - 5000 
    if (aci <= 0):
        preco = kw * 0.55
        print("Gastos de energia com base nos KW",preco)
    else:
        preco = kw * 0.60
        print("Gostos com energia com base no consumo acima do limite",preco)
elif (tipo == "X" or tipo == "x"):
    print("SAINDO...")
else:
    print("Opção Invalida!")
    
        
        
        