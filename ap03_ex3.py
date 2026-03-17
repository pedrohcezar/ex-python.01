#BOLETIM SIMPLIFICADO
nota1 = float(input("Qual a nota 1?: "))
nota2 = float(input("Qual a nota 2?: "))
nota3= float(input("Qual a nota 3?: "))

#CÁLCULO DAS VARIÁVEIS
soma = nota1 + nota2 + nota3
media = soma / 3
pontos_restantes = (30 - soma)

#RESULTADOS
print ("Relatório de notas")
print ("--------------------")
print (f"Soma das notas:{soma:.2f}")
print (f"Média :{media:.2f}")
print (f"Pontos para nota máxima:{pontos_restantes:.2f}")
