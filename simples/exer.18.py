val = float(input("Digite o valor da casa: "))
sal = float(input("Digite o salário do comprador: "))
anos = float(input("Digite em quantos será pago: "))
prest = val / (anos * 12)
lim = sal * 0.30
if prest > lim:
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")