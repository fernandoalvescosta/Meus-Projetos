n1 = int(input("Voce quer a tabuada de qual numero?: "))
inicio = int(input("Em que numero voce deseja começar a tabuada?: "))
fim = int(input(f"Voce quer a tabuada do {n1} de [{inicio}] até quanto?: "))
while inicio <= fim:
    r = inicio * n1
    print(f"{inicio} x {n1} = {r}")
    inicio +=1
