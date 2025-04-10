num1 = float(input("digite um numero:"))
num2 = float(input("digite outro numero:"))

operacao = input("escolhas a operaçao (+, -, *, /):")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 !=0:
        resultado = num1 / num2
    else: resultado = "erro divisxao zero nao pode"
else:
    resultado = "operaçao invalida"

print(f"o resultado e: {resultado}")              