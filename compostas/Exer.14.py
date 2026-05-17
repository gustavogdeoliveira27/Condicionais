temp = float(input("Digite uma temperatura: "))

if temp < 15:
    print("A temperatura está fria!")
elif 15 <= temp < 30:
    print("A temperatura está agradável!")
elif temp > 30:
    print("A temperatura está quente!")