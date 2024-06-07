import os
def limpar_tela():
    os.system('cls')

limpar_tela()
print("╔═════════════════════════════════════════════════╗\n"
      "║                Lista de exercícios              ║\n"
      "║ Exercício 1: Calcular área de um retângulo      ║\n"
      "║ Exercício 2: Calcular área de um quadrado       ║\n"
      "║ Exercício 3: Calcular valor final de um produto ║\n"
      "║ Exercício 4: Calcular a área de um círculo      ║\n"
      "║ Exercício 5: Converter reais em dólar           ║\n"
      "║ Exercício 6: Converter dólar em reais           ║\n"
      "╚═════════════════════════════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer :"))


if exercicios == 1:
    
    
    base = float(input("\n Diga qual o tamanho da base: "))
    altura = float(input(" Diga qual o tamanho da base: "))
    area = float(base*altura)
    print(f"A área do retângulo é: {area}")

if exercicios == 2:
      
     lado = float(input("\n Diga qual o tamanho do lado: "))
     area = float(lado**2)
     print(f" A área do quadrado é: {area}")
if exercicios == 3:
    
    valor= float(input("\n Se o valor de um produto é: "))
    desconto = float(input("E o desconto é: "))
    valorFinal= float(valor-valor*(desconto/100))
    print(f"O valor final do produto é: {valorFinal}")

if exercicios == 4:
    
    raio = float(input("Digite o raio: "))
    area = float(3.141592*(raio**2))
    print(f"A área do seu circulo é: {area}")

if exercicios == 5:
   
    reais = float(input("Digite o valor de reais que possui: "))
    dolar = float(reais/5.16)
    print(f"O valor em dolar do seu dinheiro é: {dolar:.2f}")

if exercicios == 6:
    print("Vamos converter dolar em reais")
    dolar = float(input("Digite o valor de dolar que possui: "))
    reais = float(dolar*5.16)
    print(f"O valor em reais do seu dinheiro é: {reais:.2f}")
