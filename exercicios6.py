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
      "╚═════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer: "))

if exercicios == 1:


 nome = input("\nDiga seu nome completo:")
 nospace = len(nome)- nome.count(" ")
 #saida de nome em letras maiusculas
 nome_maiusculo = nome.upper()
 print("\n Nome maiusculo: ", nome_maiusculo)

 #saida de nome em letars minusculas
 nome_minusculo = nome.lower()
 print("\n Nome minusculo: ", nome_minusculo)

 #contagem de caracteres
 contagem_caracteres = len(nome.replace(" "," "))
 print("\n Quantidade de letras: ", nospace)

 #quandidade de letras do primeiro nome
 primeiro_nome = nome.split()[0]
 quantidade_letras_primeiro = len(primeiro_nome)
 print("\n Quantidade de letras do primeiro nome: ", quantidade_letras_primeiro)

if exercicios == 2:
    #exemplo em string
    numero = input("\nDigite um numero de 0 a 9999")
    #completa o numero com zeros a esquerda para garantir 4 digitos
    numero = numero.zfill(4)
    #exibe cada digito separado
    print("\nMilhar: ", numero[0])
    print("\nCentena: ", numero[1])
    print("\nDezena: ", numero[2])
    print("\nUnidade: ", numero[3])
