#PLANEJAMENTO DE VIAGEM - DADOS
km = float(input("Qual a distâcia da viagem? : "))
consumo_do_carro = float(input("km/l:"))
valor_do_combustivel = float(input("Qual o preço do combustível?: (R$/litro) " ))

#CÁLCULO DAS VARIAVEIS
combustivel_necessario = km / consumo_do_carro
custo_estimado = combustivel_necessario * valor_do_combustivel

#RESULTADOS
print ("Planejamento de viagem")
print ("--------------------")
print (f"Litros necessários: {combustivel_necessario:.2f}")
print (f"Custo da viagem: {custo_estimado:.2f}")