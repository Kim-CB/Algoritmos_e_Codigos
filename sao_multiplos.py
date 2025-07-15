def verificar_multiplos(a, b):

    # Validação de entrada
    if a == 0 or b == 0:
        raise ValueError("Os valores não podem ser zero!")
    
    # Verificar se a é multiplo de b
    a_multiplo_b = (a % b == 0)

    # Verificar se b é multiplo de a
    b_multiplo_a = (b % a == 0)

    # Determinar o tipo de relação
    if a_multiplo_b and b_multiplo_a:
        relacao = "ambos_multiplos"
        mensagem = "São múltiplos"
    elif a_multiplo_b:
        relacao = "a_multiplo_b"
        mensagem = "São múltiplos"
    elif b_multiplo_a:
        relacao = "b_multiplo_a"
        mensagem = "São múltiplos"
    else: 
        relacao = "nao_multiplos"
        mensagem = "Não são múltiplos"

    return {
        'mensagem': mensagem,
        'relacao': relacao,
        'a_multiplo_b': a_multiplo_b,
        'b_multiplo_a': b_multiplo_a,
        'a': a,
        'b': b    
    }

def resultado_detalhado(resultado):
    a = resultado['a']
    b = resultado['b']

    print('---------------------------')
    print("RESULTADO DA VERIFICAÇÃO")
    print('---------------------------')

    # Resultado principal
    print(f"Valores analisados: a = {a}, b = {b}")
    print(f"Resultado: {resultado['mensagem']}")


    print('---------------------------')
    print("ANÁLISE DETALHADA")
    print('---------------------------')

    # a ser múltiplo de b
    if resultado['a_multiplo_b']:
        print(f" {a} é múltiplo de {b}")
        print(f" {a} / {b} = {a // b} (resto = {a % b})")
        print(f" {a} = {b} x {a // b}")
    else:
        print(f" {a} não é múltiplo de {b}")
        print(f" {a} / {b} = {a // b} (resto = {a % b})")
        print(f" {a} = {b} x {a // b} + {a % b}")

    # b ser múltiplo de a 
    if resultado['b_multiplo_a']:
        print(f" {b} é múltiplo de {a}")
        print(f" {b} / {a} = {a // b} (resto = {b % a})")
        print(f" {b} = {a} x {b // a}")
    else:
        print(f" {b} não é múltiplo de {a}")
        print(f" {b} / {a} = {b // a} (resto = {b % a})")
        print(f" {b} = {a} x {b // a} + {b % a}")
        

def encontrar_multiplos(numero, quantidade=10):
    # Encontrar multiplos de um numero
    multiplos = []
    for i in range(1, quantidade + 1):
        multiplos.append(numero * i)
    return multiplos

def encontrar_divisores(numero):
    # Encontrar divisores do numero
    divisores = []
    for i in range(1, abs(numero) + 1):
        if numero % i == 0:
            divisores.append(i)
            if i != numero // i:
                divisores.append(numero // i)
    if numero < 0:
        divisores_negativos = [-d for d in divisores]
        divisores.extend(divisores_negativos)
    
    return sorted(set(divisores))

def main():
    
    print("--- Verificador de Múltiplos ---")
    print("Este programa verifica se dois números são múltiplos um do outro.")
    print("\nDigite dois números inteiros (diferentes de zero):")

    try:
        a = int(input("Digite o primeiro número (a): "))
        b = int(input("Digite o primeiro número (b): "))
        
        # verificação 
        resultado = verificar_multiplos(a, b)
        # resultado detalhado
        resultado_detalhado(resultado)

        # extras
        print("---------------------------")
        print("INFORMAÇÕES EXTRA")
        print("---------------------------")

        # multiplos
        multiplos_a = encontrar_multiplos(a, 5)
        multiplos_b = encontrar_multiplos(b, 5)

        print(f"Primeiros 5 múltiplos de {a}: {multiplos_a}")
        print(f"Primeiros 5 múltiplos de {b}: {multiplos_b}")

        # divisores
        divisores_a = encontrar_divisores(a)
        divisores_b = encontrar_divisores(b)

        print(f"Divisores de {a}: {divisores_a}")
        print(f"Divisores de {b}: {divisores_b}")

        if abs(a) == abs(b):
            print(f"\nObservação: |{a}| = |{b}|, portanto são múltiplos um do outro!")
        elif abs(a) == 1 or abs(b) == 1:
            print(f"\nObservação: Um dos números é 1, que é divisor de qualquer número!")

    except ValueError as e:
        print(f"\nErro: {e}")
        print("Por favor, digite apenas números inteiros diferentes de zero!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def testes():
    print("---------------------------")
    print("TESTES")
    print("---------------------------")

    casos_teste = [
        (6, 3),
        (10, 5),
        (12, 4),
        (7, 3),
        (15, 25),
        (8, 8),
        (-12, 3),
        (9, -3),
        (100, 10),
        (17, 5)
    ]

    for i, (a, b) in enumerate(casos_teste, 1):
        print(f"\nTeste {i}: a = {a}, b = {b}")
        print("---------------------------")

        try:
            resultado = verificar_multiplos(a, b)
            print(f"Resultado: {resultado['mensagem']}")

            if resultado['a_multiplo_b']:
                print(f" {a} é múltiplo de {b}")
            else:
                print(f" {a} não é múltiplo de {b}")

            if resultado['b_multiplo_a']:
                print(f" {b} é múltiplo de {a}")
            else:
                print(f" {b} não é múltiplo de {a}")
        except ValueError as e:
            print(f" Erro: {e}")

def menu():
    while True:
        print("---------------------------")
        print("VERIFICADOR DE MÚLTIPLOS")
        print("---------------------------")
        print("1. Verificar se dois números são múltiplos")
        print("2. Encontrar múltiplos de um número")
        print("3. Encontrar divisores de um número")
        print("4. Executar testes automáticos ")
        print("5. Sair")
        print("---------------------------")

        try:
            opcao = int(input("Escolha uma opção (1 - 5): "))

            if opcao == 1:
                main()
            elif opcao == 2:
                num = int(input("Digite um número: "))
                qtd = int(input("Quantos múltiplos deseja?"))
                multiplos = encontrar_multiplos(num, qtd)
                print(f"Primeiros {qtd} múltiplos de {num}: {multiplos}")
            elif opcao == 3:
                num = int(input("Digite um número: "))
                if num == 0:
                    print("Zero não tem divisores definidos!")
                else:
                    divisores = encontrar_divisores(num)
                    print(f"Divisores de {num}: {divisores}")

            elif opcao == 4:
                testes()
            elif opcao == 5:
                print("Obrigado por usar o verificador!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("Por favor, digite apenas números!")

if __name__ == "__main__":
    menu()

        

