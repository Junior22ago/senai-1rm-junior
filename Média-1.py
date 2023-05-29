nota1= float(input("informe a nota1: "))
nota2= float(input("informe a nota2: "))
nota3= float(input("informe a nota3: "))

media= (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("APROVADO")
else:
    if media >= 5:
        print("Conselho de Classe")
    else:
        print("REPROVADO(A)")

print("A sua média foi: ",media)

