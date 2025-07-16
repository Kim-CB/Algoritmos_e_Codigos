def salario():

    print("-- CALCULADORA DE SALÁRIO --")
    print()

    try:

        horas_trabalhadas = float(input("Digite as horas trabalhadas no mês: "))

        if horas_trabalhadas <= 0:
            print("Horas trabalhadas devem ser um valor positivo.")
            return
        if horas_trabalhadas > 744:
            print("Número maior que quantidade de horas em um mês.")
        
        valor_hora = float(input("Digite o valor da hora trabalhada: R$ "))

        if valor_hora <= 0:
            print(" Valor da hora deve ser maior que 0.")
            return

        desconto = float(input("Digite o percentual de desconto: "))

        if desconto < 0 or desconto > 100:
            print("Percentual deve estar entre 0 e 100.")
            return
        
        print(f"\n-- DADOS INFORMADOS --")
        print(f"\nHoras Trabalhadas: {horas_trabalhadas:.2f} horas")
        print(f"\nValor da hora: R$ {valor_hora:.2f}")
        print(f"\nPercentual de desconto: {desconto:.2f}")

        salario_bruto = horas_trabalhadas * valor_hora

        total_de_desconto = (desconto / 100) * salario_bruto

        salario_liquido = salario_bruto - total_de_desconto

        print(f"\n--- RESUMO ---")
        print(f"Horas trabalhadas: {horas_trabalhadas:.2f}")
        print(f"SAlário Bruto: {salario_bruto:.2f}")
        print(f"Desconto: R$ {total_de_desconto:.2f} ({desconto:.2f})%")
        print(f"Salário Líquido: {salario_liquido:.2f}")

        print("\n-- EXTRAS --")
        print()
        if desconto > 30:
            print(" LIQUIDAÇÃO MALUCA !!!")
        elif 30 > desconto > 20:
            print(" PROMOÇÃO MÉDIA")
        else:
            print(" DESCONTO BAIXO")

        if horas_trabalhadas > 220: # Considerando ~220 horas como padrão mensal 
            horas_extras = horas_trabalhadas - 220
            print(f"Possíveis horas extras: {horas_extras:.2f} horas ")

    except ValueError:
        print("Por favor, digite apenas números válidos.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def menu():
    print("-- CALCULADORA DE SALÁRIO --")
    print()
 
    while True:
        print("1 - Calcular salário de um funcionário")
        print("2 - Sair ")   
        opcao = int(input("Digite: "))

        if opcao == 1:
            salario()

        elif opcao == 2:
            print("Tchau!")
            break
        else:
            print("Opção inválida, digite 1 ou 2.")

if __name__ == "__main__":
    menu()
        

