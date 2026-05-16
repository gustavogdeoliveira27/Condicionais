vel = int(input("Qual a velocidade do carro? "))
multa = (vel - 80) * 7
if vel > 80:
    print(f"Você foi multado! O valor a pagar é {multa} R$")