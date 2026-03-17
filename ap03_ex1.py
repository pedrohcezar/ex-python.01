#CONSUMO DE ENERGIA - DADOS
potencia = float(input("potência:"))
horas_de_uso = float(input("Qual o consumo diário?:"))
dias_de_uso = float(input("Quantos dias o aparelho foi utilizado?:"))
preco_da_energia = float(input("Valor da conta de luz:"))

#CALCULO DAS VARIÁVEIS
consumo_diario = (potencia * horas_de_uso)/1000
consumo_mensal = consumo_diario * 30
custo_mensal = consumo_mensal * preco_da_energia

#RESULTADOS
print ("Relatório de consumo") 
print ("--------------------") 
print (f"Consumo diário (kWh) : {consumo_diario:.2f}") 
print (f"Consumo mensal (kWh) : {consumo_mensal:.2f}") 
print (f"Custo mensal (R$): {custo_mensal:.2f}")