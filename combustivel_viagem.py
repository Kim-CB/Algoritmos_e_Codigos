

def combustivel():

    print("-- CALCULADORA CONSUMO DE COMBUSTÍVEL --")
    print("Automóvel: 12 km por litro")
    print()

    try:

        tempo =float(input("Digite o tempo gasto na viagem (em horas):"))
        velocidade = float(input("Digite a velocidade média (em km/h):"))

        if tempo <= 0 or velocidade <= 0:
            print("Tempo e velocidade devem ser positivos")
            return
        
        distancia = tempo * velocidade
        litros_usados = distancia / 12

        print("\n--- RESULTADOS ---")
        print(f"Tempo de viagem: {tempo} horas")
        print(f"Velocidade média: {velocidade} km/h")
        print(f"Distância percorrida: {distancia:.2f} km")
        print(f"Combustível utilizado: {litros_usados:.2f} litros")

    except ValueError:
        print("Digite apenas números válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def menu():
    print("-- CALCULADORA CONSUMO DE COMBUSTÍVEL --")
    print("Automóvel: 12 km por litro")
    print()

    while True:
        print("-- CALCULADORA CONSUMO DE COMBUSTÍVEL --")
        print()
        print("1 - Calcular consumo")
        print("2 - Sair")
        opcao = int(input("Digite: "))

        if opcao == 1:
            combustivel()
        elif opcao == 2:
            print("Tchau!")
            break
        else: print("Opção inválida, digite 1 ou 2.")

if __name__ == "__main__":
    menu()