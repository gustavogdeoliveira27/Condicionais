lado1 = float(input("Digite o valor de um lado do triângulo: "))
lado2 = float(input("Digite o valor de outro lado do triângulo: "))
lado3 = float(input("Digite mais um valor de um lado do triângulo: "))
if lado1 == lado2 == lado3:
    print("Seu triângulo é um Equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Seu triângulo é um Isôceles!")
else:
    print("Seu triângulo é um Escaleno!")