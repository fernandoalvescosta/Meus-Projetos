n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
print("Escolha a operação a ser feita com os numeros escolhidos!")
print("Aperte [1] para Adição (+)")
print("Aperte [2] para Subtração (-)")
print("Aperte [3] para Multiplicação (*)")
print("Aperte [4] para Divisão (/)")
print("Aperte [0] para SAIR")
escolha = int(input(":"))
if (escolha == 1):
    print("Voce escolheu Adição (+)")
    r = n1 + n2
    print (n1, "+", n2, "=",r)
elif (escolha == 2):
    print("Voce escolheu Subtração (-)")
    r = n1 - n2
    print (n1, "-", n2,"=",r)
elif (escolha == 3):
    print("Voce escolheu Multiplicação (*)")
    r = n1 * n2
    print (n1, "*", n2, "=",r)
elif (escolha == 4):
    print("Voce escolheu Divisão (/)")
    r = n1 / n2
    print (f"{n1} / {n2} = {r:.2f}")
elif escolha == 0:
    print("ENCERRADO!")
    
