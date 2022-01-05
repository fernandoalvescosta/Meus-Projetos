'''
EX2 - Crie um sistema que simule um emprestimo
'''

emprestimo = float(input("Qual o valor do empréstimo que deseja adquirir? R$"))
salario = float(input("Qual o valor da sua renda mensal? R$"))
anos = int(input("Em quantos anos deseja efetuar o pagamento? "))
meses = (anos * 12)
parcela = (emprestimo / meses)
salarioB = (salario *30/100)
if (parcela <= salarioB):
    print("Meus parabéns !! Seu emprestimo foi APROVADO !!")
    print("DADOS DO EMPRESTIMO")
    print("Valor da parcela: R$ %.2f"%parcela)
    print("Quantidade de Parcelas: ",meses)
else:
    print("Sinto muito, seu emprestimo não foi aprovado")