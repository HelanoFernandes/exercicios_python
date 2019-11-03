#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato

valor_hr = float(input("valor da sua hora: "))
total_horas = float(input("Quantas horas trabalhadas: "))

total_mes = valor_hr * total_horas

ir = (total_mes * 11) / 100
inss = (total_mes * 8) / 100
sind = (total_mes * 5) / 100

total_liq = total_mes - ir - inss - sind

print("Seu salário bruto é de: {0:.2f}".format(round(total_mes, 2)))
print("\t- IR (11%) : R${0:.2f}".format(round(ir, 2)))
print("\t- INSS (8%) : R${0:.2f}".format(round(inss, 2)))
print("\t- Sindicato ( 5%) : R${0:.2f}".format(round(sind, 2)))
print("\t\t= Salário Liquido: R${0:.2f}".format(round(total_liq, 2)))
