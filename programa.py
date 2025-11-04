from funcoes import *

listaViagens=[]

while True:
    print("BEM VINDO(A) AO CONTROLE DE VIAJENS")
    print("1 - Registrar nova viagem")
    print("2 - Exibir todas as viagens")
    print("3 - Buscar viagens por motorista")
    print("4 - Exibir viagem mais cara")
    print("5 - Mostrar media geral de consumo")
    print("0 - Sair")

    op=int(input("Digite sua escolha: "))

    if op==1:
        print(registrar_viagem(listaViagens))

    elif op==2:
        print(exibir_viagens(listaViagens))

    elif op==3:
        print(buscar_motorista(listaViagens))

    elif op==4:
        print(viagem_mais_cara(listaViagens))

    elif op==5:
        print(media_consumo(listaViagens))

    elif op==0:
        print("saindo do controle de viagens...")
        break
    else:
        print("escolhe direito")        