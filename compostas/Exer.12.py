idade = int(input("Digite sua idade: "))

if 1 <= idade <= 17:
    print("Você é de Menor.")
elif 18 <= idade <= 59:
    print("Você é Adulto.")
elif idade >  60:
    print("Você é Idoso.")