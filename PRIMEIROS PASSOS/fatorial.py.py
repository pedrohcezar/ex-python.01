#FATORIAL DE UM NÚMERO
number = float(input("Digite um número: "))

if number < 0:
    print("Fatorial não existe para número negativo")
else:
    f = 1
    n1 = 1

    while n1 <= number:
        f = f * n1
        n1 = n1 + 1

    print("O fatorial de", number, "é", f)