alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (alt * 2)
if imc > 25:
    print("Acima do peso ideal")
else:
    print("Peso dentro da normalidade")