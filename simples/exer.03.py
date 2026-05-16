valor = float(input("Digite o valor total da compra: R$ "))
if valor > 100:
    print(f"O total a pagar é: R$ {valor - (valor * 0.10)}")
elif valor <= 100:
    print("O total a pagar é R$ 100.00. Nas compras acima de R$ 100, você ganha 10% de desconto!")