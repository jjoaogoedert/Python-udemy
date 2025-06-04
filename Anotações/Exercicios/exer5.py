nota = int(input('Digite a sua nota: '))

if nota >= 9:
    print('Exelente, você tirou um A')
elif 9 > nota >= 7:
    print('Bom trabalho, você tirou um B')
elif 7 >= nota >= 5:
    print('Você passou, mas precisa melhorar. Sua nota é C')
else:
    print('Reprovado')