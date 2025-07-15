
def e_bissexto(ano):
    """
    Verifica se ano é bissexto
    Regras: divisível por 4, mas não por 10, exceto se for divisícel por 400
    """
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
def dias_no_mes(mes, ano):
    """
    Retorna o número de dias em um mês específico
    """
    if mes in [1, 3 , 5, 7, 8, 10, 12]: # Jan, Mar, Mai, Jul, Ago, Out, Dez
        return 31
    elif mes in [4, 6 , 9, 11]: # Abr, Jun, Set, Nov
        return 30
    elif mes == 2: # Fevereiro
        return 29 if e_bissexto else 28
    else:
        return 0 # Mês inválido
    

def idade_para_dias(anos, meses, dias):
    """
    Converte idade em anos, meses e dias para total de dias
    """

    total_dias = 0
    ano_atual = 2025

    # Somar dias dos anos
    for i in range(anos):
        
        ano_calculado = ano_atual - anos + i
        
        if e_bissexto(ano_calculado):
            total_dias += 366
        else:
            total_dias += 365

    # Somar dias dos meses completos
    for i in range(meses):
        mes_calculado = 12 - meses + i + 1
        if mes_calculado <= 0:
            mes_calculado += 12
            ano_mes = ano_atual -1
        else:
            ano_mes = ano_atual

        total_dias += dias_no_mes(mes_calculado, ano_mes)
    
    # Somar dias restantes
    total_dias += dias
    
    return total_dias


def main():
    print("--- Conversor de Idade para Dias ---")
    print("Digite a idade em anos, meses e dias:")

    try:
        anos = int(input("Anos: "))
        meses = int(input("Meses: "))
        dias = int(input("Dias: "))

        # Ver se números são válidos e tem sentido
        if anos < 0 or meses < 0 or meses > 11 or dias < 0 or dias > 31:
            print("Valores invalidos!")
            return
        
        total = idade_para_dias(anos, meses, dias)

        print(f"\nIdade: {anos} anos, {meses} meses, {dias} dias")
        print(f"Total em dias: {total} dias")

        # Informações extras 
        print(f"Equivale a:")
        print(f"- {total // 7} semanas e {total % 7} dias")
        print(f"- Aproximadamente {total / 365.25:.1f} anos")
    except ValueError:
        print("Por favor, digite apenas inteiros!")

# Função teste de anos bissextos
def teste_bissexto():
    print("\n -- Teste de Anos Bissextos --")
    anos_teste = [2000, 2004, 2020 ,2024 ,1900, 2100, 2023]
    for ano in anos_teste:
        resultado = "é bissexto" if e_bissexto(ano) else "não é bissexto"
        print(f"Ano {ano}: {resultado}")

if __name__ == "__main__":
    main()
    teste_bissexto()