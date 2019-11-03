#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.

peso = float(input("Qual o peso do peixe?: "))
excesso = peso - 50

if (peso > 50):
    multa = excesso * 4
    print("O peso total é de: {0}".format(peso))
    print("O peixe excede {0} quilos".format(excesso))
    print("O valor da multa é de: R${0}".format(multa))
else: 
    print ("O peso é de: {0}".format(peso)) 
