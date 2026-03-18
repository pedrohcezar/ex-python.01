#ESTIMATIVA DE TEMPO PARA LEITURA DE UM LIVRO
total_pg = float(input("Total de páginas do livro: "))
palavras_pg = float(input("Número médio de palavras por página: "))
v_media = float(input("Qual a velocidade média de leitura (palavras/p minuto): "))
tempo_disponivel = float(input("Quantidade de minutos disponível por dia para ler: "))

#CÁLCULO DAS VARIÁVEIS
total_palavras = palavras_pg * total_pg
min_necessario = tempo_disponivel / v_media
hr_necessario = min_necessario * 60
dias = hr_necessario / 24

#RESULTADOS
print ("Planejamento da leitura")
print ("---------------------------- ")
print (f"Total de palavras no livro: {total_palavras:.2f}")
print (f"Tempo total de leitura (min): {min_necessario:.2f}")
print (f"Tempo total de leitura (hr): {hr_necessario:.2f}")
print (f"Tempo estimado para terminar o livro (dias): {dias:.2f}")

