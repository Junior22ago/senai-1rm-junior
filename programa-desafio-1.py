def area(largura, comprimento):
    return largura * comprimento

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

resultado = area(largura, comprimento)
print("A área do terreno é:", resultado)
