def calcular():
    # Homens: (72.7 * altura) - 58
    # Mulheres: (62.1 * altura) - 44.7

    print("-- Calculadora de peso ideal --")
    print()

    try:
        altura = float(input("Qual a sua altura(metros): "))

        if altura <= 0 or altura > 3.0:
            print("Erro: Altura deve ser um valor positivo e realista.")
            return
        
        print("\nEscolha seu sexo:")
        print("M - Masculino")
        print("F - Feminino")
        sexo = input("Digite M ou F: ").upper().strip()

        # Validação
        if sexo not in ['M','F']:
            print("Erro: Digite apenas M para masculino ou F para feminino!")
            return
        
        if sexo == 'M':
            peso_ideal = (72.7 * altura) - 58
            formula_usada = f"(72.7 x {altura}) - 58"
        else:
            peso_ideal = (62.1 * altura) - 44.7
            formula_usada = f"(62.1 x {altura}) - 44.7"

        print(f"-- Resultado --")
        print(f"Altura: {altura:.2f} m")
        print(f"Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}")
        print(f"Fórmula utilizada: {formula_usada}")
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

        # Extra
        print("\n -- AVISO --")
        print(f"Faixa saudável: {peso_ideal-5:.2f} kg a {peso_ideal+5:.2f} kg")
        print("Consulte sempre um profissional de saúde.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para a altura!")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":


    calcular()

    while True:
        continuar = input("\nDeseja calcular para outra pessoa? (s/n) ").lower().strip()
        if continuar == 's':
            print()
            calcular()
        elif continuar == 'n':
            print("Obrigado por usar a calculadora.")
            break
        else:
            print("Digite apenas 's' para sim ou 'n' para não.")