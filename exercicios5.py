#imprime numeros de 1 a 5
#i = 1
#while i<=5:
#    print(i)
#    i+=1

#mensagem apos a conclusao do loop
#print("loop concluido")

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
      "╚═════════════════════════╝\n")
exercicios= int(input(" Digite qual exercicio deseja fazer: "))

if exercicios == 1:
    distancia = float(input("\n Qual é a distancia a ser percorrida? "))
    valor=(distancia*2.70)+5.90
    print(f"\n O valor da corrida vai ser {valor:.2f}")

if exercicios == 2:
    velocidade = float(input("\n Diga a velocidade do carro: "))
    if velocidade>100:
        veloAcima = float(velocidade-100)
        multa = float(50+8*veloAcima)
        print(f"\n Você foi multado em R${multa:.2f} por dirigir acima da velocidade permitida")

    else: 
        print("\n Você está dentro da velocidade permitida")

if exercicios == 3:
    ano = int(input("\n Diga o ano para saber se é bissesto: "))
    if ano % 4 == 0 and (ano % 100 != 0 or ano):
        print(f"\n O ano {ano} é bissesto")
    else:
        print(f"\n O ano {ano} não é bissesto")

if exercicios == 4:
    salario = float(input("\n Diga o seu salario: "))
    if salario>1420:
        aumento = (salario+ salario*(15/100))

    elif salario<= 1420:
        aumento = (salario+ salario*(30/100))

    print(f"\n Seu salario novo é {aumento:.2f}")
