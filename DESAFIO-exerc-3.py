salario = float(input("Digite o salário do funcionário do SENAI: "))

if salario > 8250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"O valor do aumento é: R${aumento:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")