n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro: "))

if n2 < n1 > n3:
    print(f"O número {n1} é maior que {n2} e {n3}")
elif n1 < n2 > n3:
    print(f"O número {n2} é maior que {n1} e {n3}")
elif n1 < n3 > n2:
    print(f"O número {n3} é maior que {n1} e {n2}")
elif n1 == n2 > n3:
    print(f"Os números {n1} e {n2} são maiores que {n3}")
elif n1 == n3 > n2:
    print(f"Os números {n1} e {n3} são maiores que {n2}")
elif n2 == n3 > n1:
    print(f"Os números {n2} e {n3} são maiores que {n1}")
else:
    print("Os números são iguais.")