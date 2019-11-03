#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#homens: (72.7*h) - 58
#mulheres: (62.1*h) - 44.7

h = float(input("Qual sua altura: "))
sexo = ''

while sexo != 'M' and sexo != 'H':
    sexo = input("H ou M: ")
    def calcIdeal(sexo, h):
        if sexo == 'H':
            return (72.7*h) - 58
        else:
            return (62.1*h) - 44.7

    if sexo != 'M' and sexo != 'H':
        print ("Escolha o sexo H ou M")
    else:
        print('Seu Peso ideal e: {0}'.format(calcIdeal(sexo, h)))