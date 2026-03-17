#PLANEJAMENTO DE ABASTECIMENTO DE UMA FROTA
distancia_media_por_entrega = float(input("Qual a distância média percorrida em cada entrega (em km)?: "))
media_entregas_por_dia = float(input("Número médio de entregas realizadas por dia: "))
dias_na_semana = float(input("Número de dias trabalhados na semana: "))
consumo_medio_por_km = float(input("Consumo médio do veículo em quilômetros por litro (km/l): "))
preco_do_combustivel = float(input("Preço do combustível em reais por litro: "))

#CÁLCULO DAS VARIÁVEIS
distancia_por_dia = distancia_media_por_entrega * media_entregas_por_dia
distancia_por_semana = distancia_por_dia * 7
combustivel_por_semana = consumo_medio_por_km * distancia_por_semana
valor_do_tanque_semana = preco_do_combustivel * combustivel_por_semana

#RESULTADOS
print ("Relatório de operação do veículo")
print ("------------")
print (f"Distância diária : {distancia_por_dia:.2f}")
print (f"Distância semanal : {distancia_por_semana:.2f}")
print (f"Combustível necessário na semana (litros) : {combustivel_por_semana:.2f}")
print (f"Custo semanal do combustível (R$) : {valor_do_tanque_semana:.2f}")




