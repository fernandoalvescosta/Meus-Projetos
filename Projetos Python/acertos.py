'''
EX1 - Criar um sistema que conte quantas questoes um usuario acertou
'''
total = 0
print("RESPONDA CORRETAMENTE")
print("-----------------------")
print("1 - UMA PERGUNTA MUITO DIFICIL")
print("A - ")
print("B - ")
print("C - ")
print("D - ")
print("E - ")
r1 = str(input("INSIRA SUA RESPOSTA: "))         
if (r1 == 'B') or (r1 == 'b'):
    print("RESPOSTA CORRETA!!")
    total +=1
else:
    print("RESPOSTA INCORRETA !!")

print("2 - UMA PERGUNTA MUITO DIFICIL")
print("A - ")
print("B - ")
print("C - ")
print("D - ")
print("E - ")
r2 = str(input("INSIRA SUA RESPOSTA: "))
if (r2 == 'A') or (r2 == 'a'):
    print("RESPOSTA CORRETA!!")
    total +=1
else:
    print("RESPOSTA INCORRETA !!")
    
print("3 - UMA PERGUNTA MUITO DIFICIL")
print("A - ")
print("B - ")
print("C - ")
print("D - ")
print("E - ")
r3 = str(input("INSIRA SUA RESPOSTA: "))
if (r3 == 'D') or (r3 == 'd'):
    print("RESPOSTA CORRETA!!")
    total +=1
else:
    print("RESPOSTA INCORRETA !!")

print("Toral de respostas corretas: ",total)
