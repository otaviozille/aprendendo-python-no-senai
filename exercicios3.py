import os
def limpar_tela():
    os.system('cls')

limpar_tela()
print("╔═══════════════════════════════════════════════════════════════════════════╗\n"
      "║                           Lista de exercícios                             ║\n"
      "║ Exercício  1: Leia 3 valores e fale se a soma de A e B é menor que C      ║\n"
      "║ Exercício  2: Leia A e B, se iguais some-os, se não multiplique-os        ║\n"
      "║ Exercício  3: Leia um valor e imprima seu antecessor e sucessor           ║\n"
      "║ Exercício  4: Leia um salário, diga quantos salários minímos ele equivale ║\n"
      "║ Exercício  5: Leia um valor e imprima o reajuste de 5%                    ║\n"
      "║ Exercício  6: Leia 2 números e diga qual é maior                          ║\n"
      "║ Exercício  7: Leia 3 valores e imprima-os em ordem decrescente            ║\n"
      "║ Exercício  8: Leia 3 valores e imprima a média aritmética deles           ║\n"
      "║ Exercício  9: Calcule o fatorial de um número inteiro não negativo        ║\n"
      "║ Exercício 10: Leia um número e identique se ele é um número primo         ║\n"
      "╚═══════════════════════════════════════════════════════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer: "))


if exercicios == 1:
    #Entrada de valores e soma
    A = float(input("\n Diga o valor de A: "))
    B = float(input("\n Diga o valor de B: "))
    C = float(input("\n Diga o valor de C: "))
    soma = float(A+B)
    #Teste para saber se é menor
    if soma < C:
         print(f"\nO valor da soma é {soma} e é menor que C")
    else:print(f"\nO valor da soma é {soma} e não é menor que C") 

if exercicios == 2:
    #Entrada de valores
    A = int(input("\n Diga o valor de A: "))
    B = int(input("\n Diga o valor de B: "))
    soma = int(A+B)
    multiplicacao = (A*B)
    #Verificação de variaveis
    if A == B:
        C = int(soma)

        print(f"\n O valor de C é: {C}")

    else: 
     C = int(multiplicacao) 
     print(f"\n O valor de C é: {C}")

if exercicios == 3:
    #Entrada de valores
    numero = int(input("\n Diga o  valor do número: "))
    #Calculo de antecessor e sucessor
    antecessor = int(numero - 1)
    sucessor = int(numero + 1)
    #Saida de informaçao
    print(f"\n O valor do antecessor é {antecessor}"
          f" o valor do número é {numero} "
          f"e o valor do sucessor é {sucessor} ")
    

if exercicios == 4:
    #Entrada de informação
    salario = float(input("\n Diga o seu salário: "))
    salarioMinimo = float(1293.20)
    #Calculo de salarios
    quantidade = float(salario/salarioMinimo)
    #Saida de informaçao
    print(f"\n Seu salário corresponde a {quantidade:.2f} salários minímos")

if exercicios == 5:
    #Entrada de informação
    numero = float(input("\n Diga o valor: "))
    #Calculo de reajuste
    reajuste = float(numero + (numero*(5/100)) )
    #Saida de informaçao
    print(f"\n O valor do reajuste é {reajuste}")
if exercicios == 6:
    #Entrada de informação
    A = int(input("\n Diga o valor de A: "))
    B = int(input("\n Diga o valor de B: ")) 
    #Teste de variaveis
    if A > B:
        print("\n O valor de A é maior")  
    elif A < B:
        print("\n O valor de B é maior")

if exercicios == 7:
    #Entrada de informação
    A = int(input("\n Diga o valor do primeiro número: "))
    B = int(input("\n Diga o valor do segundo número: "))
    C = int(input("\n Diga o valor do terceiro número: "))
    #Verificação de maximo,meio e minimo
    maior = max(A,B,C)
    menor = min(A,B,C)
    meio =  (A+B+C -maior -menor)
    #impressao dos numeros de forma decrescente
    print(f"\n Os valores em ordem decrescente são {maior}, {meio} e {menor}")

if exercicios == 8:
    #Entrada de informação
    A = float(input("\n Diga o valor para A: "))
    B = float(input("\n Diga o valor para B: "))
    C = float(input("\n Diga o valor para C: ")) 
    #Calculo de media
    media = float((A+B+C)/3) 
    #Saida da resposta
    print(f"\n O valor da média é: {media}")  

if exercicios == 9:
    #Entrada de valores
 numero = int(input("\n Diga o número: "))
 resultado = 1
 #Teste para ver se o fatorial funciona 
 if numero < 0:
    print("O fatorial não está definido para números negativos.")
    #Fatorial de 0
 elif numero == 0:
    print("O fatorial de 0 é 1.")
    #Calculo de fatorial
 else:
    for i in range(1, numero + 1):
        resultado *= i
        #resultado
    print(f'O fatorial de {numero} é: {resultado}')



if exercicios == 10:
    #Entrada de valores
    numero = int(input("Digite um número inteiro positivo: "))
    #Testa se o numero é menor ou igual a 1
    if numero <= 1:
        print(F"\n {numero} não é um número primo.")
    else:
    #Teste para saber se o numero é primo
     for i in range(2, int(numero**0.5) + 1):
        #Se o número for divisível por algum número menor que ele mesmo, não é primo
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
        #Se o numero for divisivel somente por ele mesmo e 1, é primo
     else:
        print(f"{numero} é um número primo.")

if exercicios == 11:
    letras = str(input("\n Diga uma letra: "))

    if letras in 'aeiouAEIOU' :
        print(f"\n é vogal ")
    
    else:
        print("\n é consoante")

if exercicios == 12:
    A = float(input("\n Diga um numero: "))
    B = float(input("\n Diga um numero: "))
    C = float(input("\n Diga um numero: "))
    
    maior = max(A,B,C)

    print(f"\n O maior numero é {maior}")

if exercicios == 13:
    A = int(input("\n Diga o valor do primeiro número: "))
    B = int(input("\n Diga o valor do segundo número: "))
    C = int(input("\n Diga o valor do terceiro número: "))
    #Verificação de maximo e minimo
    maior = max(A,B,C)
    menor = min(A,B,C)

    print(f"\n Os valores  são {maior} e {menor}")

if exercicios == 14:
    # Solicitar ao usuário para digitar dois números inteiros
 numero1 = int(input("Digite o primeiro número inteiro: "))
 numero2 = int(input("Digite o segundo número inteiro: "))

 # Exibir os valores originais
 print(f"Valores originais: Numero1 = {numero1}, Numero2 = {numero2}")

 # Usar if e else para trocar os valores
 if numero1 != numero2:
    # Trocar os valores se eles forem diferentes
    temp = numero1
    numero1 = numero2
    numero2 = temp
 else:
    # Se os valores forem iguais, a troca não faz diferença
    print("Os números são iguais, a troca não é necessária.")

 # Exibir os novos valores
 print(f"Valores trocados: Numero1 = {numero1}, Numero2 = {numero2}")





        




    
       
