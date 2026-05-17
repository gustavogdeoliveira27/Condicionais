valor = float(input("Digite o valor da compra: "))

if valor <= 100:
    print(f"O total a pagar é R$ {valor}.")
elif 100 < valor <= 200:
    print(f"Parabéns! Você recebeu um desconto de 10% na compra! O total a pagar é R$ {valor - (valor * 0.10)}.")
elif valor > 200:
    print(f"Parabéns!! Você recebeu um desconto de 20% na compra! O total a apagar é R$ {valor - (valor * 0.20)}.")