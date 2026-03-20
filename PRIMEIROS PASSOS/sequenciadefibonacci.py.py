#SEQUÊNCIA  DE FIBONACCI

#DEFINE OS NÚMEROS
number1 = int(input("INSIRA O PRIMEIRO NÚMERO: "))
number2 = int(input("INSIRA O SEGUNDO NÚMERO: "))

#CONDIÇÃO DAS VARIÁVEIS
if number1 and number2 <=0 :
    print ("Tente Novamente")

#CÁLCULO DA SEQUÊNCIA
number3 = number1 + number2
number4 = number2 + number3
number5 = number3 + number4
number6 = number4 + number5
number7 = number5 + number6
number8 = number6 + number7
number9 = number7 + number8
seq = print (number3, number4, number5, number6, number7, number8, number9)