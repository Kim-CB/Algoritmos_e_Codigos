## Complicando o simples

import math


def expressao(a, b, c):

    if a <= 0 or b<= 0 or c <= 0:
        raise ValueError("Todos os valores devem ser números inteiros positivos")
    
    r = (a + b) ** 2

    s = (b + c ) ** 2

    d = (r + s) / 2

    return r, s, d

def main():
    # Enfeitando um trabalho simples. Porque?  sei lá.... 
    print("--- Calculadora de Expressão ----")
    print("Fórmula: D = (R + S) / 2")
    print("onde R = (A + B)² e S = (B + C)²")
    print("\nDigite três números inteiros positivos: ")

    try:
        a = int(input("Digite o valor de A: "))
        b = int(input("Digite o valor de B: "))
        c = int(input("Digite o valor de C: "))

        r, s, d = expressao(a, b, c)

        print(f"\n----------------------")
        print(f"Resultados:")
        print(f"------------------------")
        print(f"Valores de entrada:")
        print(f"A = {a}")
        print(f"B = {b}")
        print(f"C = {c}")
        print(f"\nResultado final:")
        print(f" D = (R + S) / 2 = ({r} + {s}) / 2 = {r + s} / 2 = {d}")

        print(f"\n----------------------")
        print(f"Informações Extras:")
        print(f"------------------------")
        print(f" D como número inteiro: {int(d)}")
        print(f" D arrendondado: {round(d, 2)}")
        print(f" Raiz quadrada de D: {math.sqrt(d):.2f}")

        if d == int(d):
            print(f" D é um número inteiro!")
        else: print(f" D é um número decimal!")

    except ValueError as e:
        print(f"\nErro: {e}")
        print(f"Por favor, digite apenas números inteiros positivos!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def testes():
    # Testes automáticos com diferentes valores
    print(f"\n---------------------")
    print("Testes Automáticos")
    print(f"\n---------------------")

    casos_testes = [
        (1, 2, 3), # Caso Simples
        (2, 3, 4), # Caso médio 
        (5, 10, 15), # Números maiores
        (1, 1, 1), # Números iguais 
        (10, 5, 2) # Ordem decrescente
    ]

    for i,(a, b, c) in enumerate(casos_testes, 1):
        print(f"\nTeste {i}: A={a}, B={b}, C={c}")
        try:
            r, s, d = expressao(a, b, c)
            print(f" R = ({a} + {b})² = {r}")
            print(f" S = ({b} + {c})² = {s}")
            print(f" D = ({r} + {s})² = {d}")
        except ValueError as e:
            print(f" Erro: {e}")

def passo_a_passo(a, b, c):
    # Versão detalhada

    print("------------------------------")
    print("Cálculo passo a passo")
    print("-------------------------------")

    print(f"Dados de entrada: A = {a}, B = {b}, C = {c}")

    # Passo 1: Calcular A + B
    soma_ab = a + b
    print(f"\nPasso 1: Calcular A + B")
    print(f" A + B = {a} + {b} = {soma_ab}")
    
    
    # Passo 2: Calcular R = (A + B)²
    r = soma_ab ** 2
    print(f"\nPasso 2: Calcular R = (A + B)²")
    print(f" R = ({soma_ab})² = {r}")

    # Passo 3: Calcular B + C
    soma_bc = b + c
    print(f"\nPasso 3: Calcular B + C")
    print(f" B + C = {b} + {c} = {soma_bc}")

    # Passo 4: Calcular S = (B + C)²
    s = soma_bc ** 2 
    print(f"\nPasso 4: Calcular S = (B + C)²")
    print(f"  S = ({soma_bc})² = {s}")

    # Passo 5: Calcular R + S
    soma_rs = r + s
    print(f"\nPasso 5: Calcular R + S")
    print(f" R + S = {r} + {s} = {soma_rs}")

    # Passo 6: Calcular D = (R + S) / 2
    d = soma_rs / 2
    print(f"\nPasso 6: Calcular D = (R + S) / 2")
    print(f" D = {soma_rs} / 2 = {d}")

    print("-----------------------------")
    print(f"Resultado Final: D = {d}")
    print("-----------------------------")

    return d

def menu_interativo():
    """
    Menu Interativo
    """

    while True:
        print("\n---------------------------------------")
        print("Calculadora de expressão Matemática")
        print("-----------------------------------------")
        print("1. Calcular expressão")
        print("2. Calcular com passo a passo")
        print("3. Executar testes automáticos")
        print("4. Sair")
        print("------------------------------------------")

        try: 
            opcao = int(input("Escolha um opção(1-4): "))

            if opcao == 1:
                main()
            elif opcao == 2:
                print("\nDigite três números inteiros positivos:")
                a = int(input("Digite o valor de A: "))
                b = int(input("Digite o valor de B: "))
                c = int(input("Digite o valor de C: "))

                if a > 0 and b > 0 and c > 0:
                    passo_a_passo(a, b, c)
                else:
                    print("Erro: Todos os valores devem ser positivos!")
            elif opcao == 3:
                testes()
            elif opcao == 4:
                print("Obrigado por usar a calculadora!")
                break
            else: print("Opção inválida! Escolha entre 1 e 4.")
        
        except ValueError:
            print("Por favor, digite apenas números!")

if __name__ == "__main__":
    menu_interativo()