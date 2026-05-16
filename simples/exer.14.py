sal = float(input("Digite seu salário: "))
if sal > 1621.00:
    print(f"Com o aumento seu salário vai para {sal + (sal * 0.10)} R$")
elif sal <= 1621.00:
    print(f"Com o aumento seu salário vai para {sal + (sal * 0.15)} R$")