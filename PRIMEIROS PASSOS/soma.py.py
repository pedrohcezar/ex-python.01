#SOMA DOS VALORES
number = int(input("Digite um número: "))
soma = 0

#CONDIÇÃO

while number != 0:
    soma = soma + number
    number = int(input("Idigite outro número: "))
print (soma)