nota = float(input("Digite uma nota: "))
if nota >= 9.0:
    print("Parabéns!!Você foi aprovado!")
elif  7.0 <= nota <= 8.9:
    print("Aprovado.")
elif 4.0 <= nota <= 6.9:
    print("Em Recuperação.")
elif nota < 4.0:
    print("Reprovado.")