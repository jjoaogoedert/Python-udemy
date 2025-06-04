saudacao = int(input("Digite para saber que horas são, para informar a saudação: "))

if saudacao <= 12:
    print("Bom dia")
elif 12 < saudacao <= 18:
    print("Boa tarde")
else:
    print("Boa noite")