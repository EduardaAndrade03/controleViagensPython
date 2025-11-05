from tabulate import tabulate


def registrar_viagem(listaViagens):
    motorista=str(input("Digite o nome do motorista: "))
    destino=str(input("qual o seu destino: "))
    distancia=float(input("quantos kilometros de distancia: "))
    combustivel_valor=float(input("qual o valor gasto com o combustivel: "))
    consumo = combustivel_valor/distancia
    viagem={
        "motorista": motorista, 
        "destino": destino, 
        "distancia": distancia, 
        "gasto": combustivel_valor, 
        "consumo": consumo
    }
    listaViagens.append(viagem)

def exibir_viagens(listaViagens):
    return tabulate(listaViagens, headers = "keys")

def  buscar_motorista(listaViagens):
    buscarmotorista=str(input("qual o motorista que deseja ver as viagens: "))
    print(f"o motorista {buscarmotorista} tem as seguintes viagens registradas: ")
    for m in listaViagens:
        if m["motorista"]==buscarmotorista:
            print(m["destino"])
    return 

def viagem_mais_cara(listaViagens):
    if len(listaViagens)==1:
            mgviagem={
                "viagem": listaViagens[0]["destino"],
                "valor": listaViagens[0]["gasto"]
            }
            return f"há apenas uma viagem registrada: {mgviagem}"
    else:
        maiorgasto=listaViagens[0]["gasto"]
        for v in listaViagens:
            if v["gasto"]>maiorgasto:
                maiorgasto=v["gasto"]
                mgviagem={
                    "viagem": v["destino"],
                    "valor": maiorgasto
                }
    return mgviagem

def media_consumo(listaViagens):
    somaconsumos=0
    for v in listaViagens:
        somaconsumos+=v["consumo"]
    mediaconsumos=somaconsumos/len(listaViagens)
    return f"A média geral de consumo entre todas as viagens é: {mediaconsumos}"
