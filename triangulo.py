import math

def triangulo():

    print("-- PROGRAMA TRIANGULO --")
    print()
    print("Digite os três lados de possível triângulo: ")

    try:
        a = float(input("Digite o valor do lado A: "))
        b = float(input("Digite o valor do lado B: "))
        c = float(input("Digite o valor do lado C: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Todos os valores devem ser positivos.")
            return
        
        print(f"\nValores informados: A = {a}, B = {b}, C = {c}")

        # Condições para formar triângulo
        condicao_ab = a + b > c
        condicao_ac = a + c > b
        condicao_bc = b + c > a

        if condicao_ab and condicao_ac and condicao_bc:
            print(f"VALORES FORMAM UM TRIÂNGULO!")

            # Teorema de Herão 
            s = (a + b + c) / 2
            # EXTRAS 
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimetro = a + b + c

            print(f"\n -- CLASSIFICAÇÃO --")
            if a == b == c:
                tipo = "Equilátero (todos os lados iguais)"
            elif a == b or a == c or b == c:
                tipo = "Isósceles (dois lados iguais)"
            else:
                tipo = "Escaleno (todos os lados diferentes)"

            print(f"Tipo: {tipo}")
            print(f"\n-- EXTRAS --")
            print(f"Perímetro: {a} + {b} + {c} = {perimetro}")
            print(f"Área: {area:.4f}")

        else:
            print(f"\n OS VALORES NÃO FORMAM UM TRIÂNGULO!")
            

            if not condicao_ab:
                print(f"Condição que não foi satisfeita: {a} + {b} = {a + b} não é maior que {c}")
            if not condicao_ac:
                print(f"Condição que não foi satisfeita: {a} + {c} = {a + c} não é maior que {b}")
            if not condicao_bc:
                print(f"Condição que não foi satisfeita: {b} + {c} = {b + c} não é maior que {a}") 
    except ValueError:
        print("Por favor, digite apenas números realisticos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def menu():

    while True:
        print("-- VALIDAR TRIANGULO --")
        print("1 - Verificar um triângulo")
        print("2 - Sair")
        opcao = int(input("Digite um opção (1 ou 2):"))

        if opcao == 1:
            triangulo()
        elif opcao == 2:
            print("Tchau!")
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")

if __name__ == "__main__":
    menu()

