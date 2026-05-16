temp = float(input("Digite a temperatura em graus Celsius: "))
f = "Fahrenheit"
k = "Kelvin"
conv = input("Gostaria de converter para Fahrenheit ou Kelvin? ")
if conv == f:
    print(f"O resultado fica {(temp * 9/5) + 32} F")
elif conv == k:
    print(f"O resultado fica {temp + 273.15} K")