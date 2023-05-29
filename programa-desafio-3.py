def maior(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    elif(num3 > num1 and num3 > num2):
        return num3

valor1= int(input("Digite o primeiro valor: "))
valor2= int(input("Digite o segundo valor: "))
valor3= int(input("Digite o terceiro valor: "))

valor_maior= maior(valor1, valor2, valor3)
print ("O maior valor é: ",valor_maior)