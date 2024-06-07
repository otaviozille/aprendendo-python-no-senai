import os
def limpar_tela():
    os.system('cls')

limpar_tela()
print("╔═════════════════════════╗\n"
      "║  Lista de exercícios    ║\n"
      "║           1             ║\n"
      "║           2             ║\n"
      "║           3             ║\n"
      "║           4             ║\n"
      "║           5             ║\n"
      "║           6             ║\n"
      "║           7             ║\n"
      "║           8             ║\n"
      "║           9             ║\n"
      "║           10            ║\n"
      "║           11            ║\n"
      "║           12            ║\n"
      "║           13            ║\n"
      "╚═════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer: "))

if exercicios == 1:
    A = float(input("\n Diga o valor da nota: "))
    B = float(input("\n Diga o valor da nota: "))
    C = float(input("\n Diga o valor da nota: "))

    media = ((A+B+C)/3)
    
    if media >= 7:
        print("\n Você está aprovado")
    
    else:
        print("\n Melhore meus 10, vc é burro")

if exercicios == 2:
 celsius = float(input("\n Diga a temperatura: "))

 fahrenheit = ((celsius*9)/5 + 32)
 print(f"\n A temperatura em fahrenheit é: {fahrenheit}")

if exercicios == 3:
    A = float(input("\n Diga o valor da nota: "))

    if A < 0:
        print("\n Esse número é negativo")

    elif A == 0:
        print("\n Esse número é 0")

    else:
        print("\n Esse número é positivo")

if exercicios == 4:
    salrio = float(input("\n Diga o valor do salario: "))
    aumento = float(input("\n Diga o valor do aumento: "))

    salarioNovo = (salrio + aumento)

    print(f"\n Seu novo salário é: {salarioNovo}")

if exercicios == 5:
    idade = int(input("\n Diga sua idade: "))

    if idade < 18:
        print("\n Você é menor de idade")

    else:
        print("\n Você é maior de idade")

if exercicios == 6:
    # Solicitar ao usuário para digitar três números
 numero1 = float(input("Digite o primeiro número: "))
 numero2 = float(input("Digite o segundo número: "))
 numero3 = float(input("Digite o terceiro número: "))

 # Verificar qual é o maior número usando if e else
 if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
 elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
 else:
    maior = numero3

 # Exibir o maior número
 print(f"O maior número é: {maior}")


if exercicios == 7:
    # Solicitar ao usuário para digitar o peso e a altura
 peso = float(input("Digite seu peso em kg: "))
 altura = float(input("Digite sua altura em metros: "))

 # Calcular o IMC
 imc = peso / (altura ** 2)

 # Determinar a categoria do IMC usando if e else
 if imc < 18.5:
    categoria = "abaixo do peso"
 elif 18.5 <= imc < 24.9:
    categoria = "com peso normal"
 elif 25 <= imc < 29.9:
    categoria = "com sobrepeso"
 elif 30 <= imc < 39.9:
    categoria = "com obesidade"
 else:
    categoria = "com obesidade mórbida"

 # Exibir o resultado
 print(f"Seu IMC é: {imc:.2f}")
 print(f"Você está {categoria}.")


if exercicios == 8:
    # Solicitar ao usuário para digitar dois números
 numero1 = float(input("Digite o primeiro número: "))
 numero2 = float(input("Digite o segundo número: "))

 # Realizar as quatro operações básicas
 soma = numero1 + numero2
 subtracao = numero1 - numero2
 multiplicacao = numero1 * numero2
 if numero2 != 0:
    divisao = numero1 / numero2
 else:
    divisao = "Indefinida (divisão por zero não é permitida)"

 # Imprimir os resultados
 print(f"Soma: {numero1} + {numero2} = {soma}")
 print(f"Subtração: {numero1} - {numero2} = {subtracao}")
 print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
 print(f"Divisão: {numero1} / {numero2} = {divisao}")

if exercicios == 9:
 # Solicitar ao usuário para digitar a idade
 idade = int(input("Digite sua idade: "))

 # Determinar a faixa etária usando if e else
 if idade < 0:
    faixa_etaria = "Idade inválida"
 elif 0 <= idade <= 2:
    faixa_etaria = "bebê"
 elif 3 <= idade <= 12:
    faixa_etaria = "criança"
 elif 13 <= idade <= 17:
    faixa_etaria = "adolescente"
 elif 18 <= idade <= 64:
    faixa_etaria = "adulto"
 else:
    faixa_etaria = "idoso"

 # Exibir a faixa etária
 print(f"Você é considerado um(a) {faixa_etaria}.")


if exercicios == 10:
    # Solicita os três números ao usuário
 a = float(input("Digite o primeiro lado do triângulo: "))
 b = float(input("Digite o segundo lado do triângulo: "))
 c = float(input("Digite o terceiro lado do triângulo: "))

 # Verifica se os números podem formar um triângulo
 if a + b > c and a + c > b and b + c > a:
    # Classifica o triângulo
    if a == b == c:
        print("Os lados fornecidos formam um triângulo equilátero.")
    elif a == b or b == c or a == c:
        print("Os lados fornecidos formam um triângulo isósceles.")
    else:
        print("Os lados fornecidos formam um triângulo escaleno.")
 else:
    print("Os lados fornecidos não podem formar um triângulo.")


if exercicios == 11:
    # Solicita o preço do produto ao usuário
 preco_original = float(input("Digite o preço do produto: R$ "))

 # Solicita a porcentagem de desconto ao usuário
 desconto = float(input("Digite a porcentagem de desconto (sem o símbolo %): "))

 # Calcula o valor do desconto
 valor_desconto = (preco_original * desconto) / 100

 # Calcula o preço final com o desconto aplicado
 preco_final = preco_original - valor_desconto

 # Imprime o resultado
 print(f"O preço final com o desconto é: R$ {preco_final:.2f}")

if exercicios == 12:

 # Solicita o nome e a idade da primeira pessoa
 nome1 = input("Digite o nome da primeira pessoa: ")
 idade1 = int(input("Digite a idade da primeira pessoa: "))

 # Solicita o nome e a idade da segunda pessoa
 nome2 = input("Digite o nome da segunda pessoa: ")
 idade2 = int(input("Digite a idade da segunda pessoa: "))

 # Determina quem é mais velho e imprime o nome
 if idade1 > idade2:
    print(f"{nome1} é mais velho(a).")
 elif idade2 > idade1:
    print(f"{nome2} é mais velho(a).")
 else:
    print(f"{nome1} e {nome2} têm a mesma idade.")

if exercicios == 13:
    # Solicita o valor da compra e o valor pago pelo cliente
 valor_compra = float(input("Digite o valor da compra: R$ "))
 valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

 # Calcula o troco
 troco = valor_pago - valor_compra

 # Verifica se o valor pago é suficiente
 if troco >= 0:
    print(f"Troco a ser devolvido: R$ {troco:.2f}")
 else:
    print("O valor pago é insuficiente para cobrir o custo da compra.")

