temperatura = int(input("Digite uma temperatura: "))

if temperatura < 10:
    print("Muito frio")
elif 10 <= temperatura < 20:
    print("Está fresco")
else:
    print("Está quente")