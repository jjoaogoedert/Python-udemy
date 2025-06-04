valor = int(input("Digite um valor para calcular o desconto: "))
desconto = 0

if valor > 100:
    desconto = (valor * 5) / 100
if 200 >= valor >= 100:
    desconto = (valor * 10) / 100
else:
    desconto = (valor * 20) / 100

print(f"O valor com o desconto de {desconto} fica {valor - desconto}")
