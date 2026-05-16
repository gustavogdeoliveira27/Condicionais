num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}!")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}!")
elif num1 == num2:
    print("Os números são iguais!")