#VALOR FINAL DE UM PRODUTO ONLINE - DADOS
preco_do_produto = float(input("Qual o valor do produto? :"))
percentual_do_imposto = float(input("Qual a porcentagem do imposto (0 a 100)? :"))
valor_do_frete = float(input("Qual o valor do frete? :"))

#CÁLCULO DAS VARIÁVEIS
produto_com_imposto = (preco_do_produto / percentual_do_imposto) + preco_do_produto
imposto = produto_com_imposto - preco_do_produto
vt = produto_com_imposto + valor_do_frete

#RESULTADO
print ("Resumo da compra")
print ("--------------------")
print (f"Valor do imposto: {imposto:.2f}")
print (f"Valor total {vt:.2f}")