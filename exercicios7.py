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
      "╚═════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer: "))

if exercicios == 1:
    #pede ao usuario o valor do salario
    salario = float(input("Digite o valor do salario: "))
    #pede ao usuario o valor do apartamento
    apartamento = float(input("Digite o valor do apartamento: "))
    #pergunta em quantos anos o usuario pretende pagar o apartamento
    anos = int(input("Em quantos anos você pretende pagar o apartamento? "))
    #calcula o valor da parcela
    parcela = apartamento / (anos * 12)
    #verifica se o valor da parcela é maior que 30% do salario
    if parcela > (salario * 0.3):
        print("Você não pode comprar o apartamento pois a parcela é maior que 30%% do seu salario")
    else:
         print("Você pode comprar o apartamento pois a parcela é menor que 30%% do seu salario")

if exercicios == 2 :
    #adicione 12% de juros ao ano e mostra todos os resultados anteriores, atualizados
    #pede ao usuario o valor do salario
    salario = float(input("Digite o valor do salario: "))
    #pede ao usuario o valor do apartamento
    apartamento = float(input("Digite o valor do apartamento: "))
    #pergunta em quantos anos o usuario pretende pagar o apartamento
    anos = int(input("Em quantos anos você pretende pagar o apartamento? "))
    #calcula o valor da parcela
    parcela = apartamento / (anos * 12)
    #calcula o valor da parcela com juros
    parcela_juros = parcela * 1.12
    #verifica se o valor da parcela é maior que 30% do salario
    if parcela_juros > (salario * 0.3):
        print("Você não pode comprar o apartamento pois a parcela é maior que 30%"" do seu salario")
    else:
        print("Você pode comprar o apartamento pois a parcela é menor que 30% do seu salario")

if exercicios == 3:
    #pede ao usuario o numero inteiro
    num = int(input("Digite um numero inteiro: "))
    #pede ao usuario qual sera a base de conversao
    base = int(input("Digite a base de conversao (2 para binario, 8 para octal, 16 para hexadecimal): "))
    if base == 2 :
        print(bin(num)[2:])
    elif base == 8 :
         print(oct(num)[2:])
    elif base == 16 :
          print(hex(num)[2:])
    else :
         print("Base de conversao invalida")

if exercicios == 4:
    #peça o ano de nascimenro do usurario
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    #informe de acordo com a idade se ele ainda vai se alistar (< 18 anos)
    #se ja pode se alistar (18 anos)
    #se ja passou da hora de alistar (> 18 anos)
    #e mostre quantos anos falta
    ano_atual = int(2024)
    idade = ano_atual - ano_nascimento
    if idade < 18 :
        print("Você ainda vai se alistar. Faltam {} anos.".format(18 - idade))
    elif idade == 18:
        print("Você ja pode se alistar.")
    else :
        print("Você ja passou da hora de alistar. Jase passou {} anos.".format(idade - 18))

if exercicios == 5:
    #peça ao usuario seu ano de nascimento
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(2024)
    idade = ano_atual - ano_nascimento
    #verifica qual categoria de natação o usuario se enquadra
    if idade < 9 :
        print("Você se enquadra na categoria Mirim")
    elif idade > 9 and idade < 14 :
        print("Você se enquadra na categoria Infantil")
    elif idade > 14 and idade < 19:
        print("Você se enquadra na categoria Juvenil")
    elif idade > 19 and idade < 22:
        print("Você se enquadra na categoria senior")
    else:
        print("Você se enquadra na categoria Master")

if exercicios == 6:
    #peça ao usuario para digitar uma frase qualquer
    frase = input("Digite uma frase qualquer: ")
    #verifica se ela é um palindromo 
    frase = frase.replace(" ", "")
    frase = frase.lower()
    if frase == frase[::-1]:
        print("A frase é um palindromo")
    else :
            print("A frase não é um palindromo")

