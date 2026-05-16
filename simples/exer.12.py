dist = float(input("Quantos quilômetros deseja percorrer? "))
if dist <= 200:
    print(f"O valor da passagem é {dist * 0.50} R$.")
elif dist > 200:
    print(f"O valor da é {dist * 0.45} R$.")