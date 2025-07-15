# usei como exemplo e objetivo de trabalho https://pt.planetcalc.com/7933/


# iguais questão anterior
def e_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30 
    elif mes == 2:
        return 29 if e_bissexto(ano) else 28
    else: return 0

def dias_para_idade(total_dias):
    """
    Converte total de dias
    """

    if total_dias < 0:
        return 0, 0, 0
    
    anos = 0
    meses = 0
    dias_restantes = total_dias
    ano_atual = 2025 

    # Anos Completos
    while dias_restantes > 0:
        dias_no_ano = 366 if e_bissexto(ano_atual - anos) else 365
        if dias_restantes >= dias_no_ano:
            dias_restantes -= dias_no_ano
            anos += 1
        else: break

    # Meses Completos
    mes_atual = 1
    ano_para_mes = ano_atual - anos

    while dias_restantes > 0 and mes_atual <= 12:
        dias_no_mes_atual = dias_no_mes(mes_atual, ano_para_mes)

        if dias_restantes >= dias_no_mes_atual:
            dias_restantes -= dias_no_mes_atual
            meses += 1
            mes_atual += 1
        else: break

    dias_finais = dias_restantes
    
    # Casos especiais
    if meses >= 12:
        anos += meses // 12
        meses = meses % 12

    return anos, meses, dias_finais


def idade(total_dias):
    
    anos_aprox = total_dias / 365.25
    meses_aprox = (total_dias % 365.25) / 30.44
    dias_aprox = total_dias % 30.44

    return anos_aprox, meses_aprox, dias_aprox

def main():
    print("-- Conversor de dias para Anos e Meses e dias --")
    print("Digite o total de dias vividos:")

    try: 
        total_dias = int(input("Total de dias: "))
        if total_dias < 0:
            print("Número de dias não pode ser negativo!")
            return
    
        anos, meses, dias =  dias_para_idade(total_dias)

        # Apresentação de dos dados
        print(f"\nInformações: ")
        print(f"Equivale a {total_dias // 7} semanas e {total_dias % 7} dias")
        print(f"Aproxidamente {total_dias / 365.25:.2f} anos")

        # Verificação
        dias_verificacao = verificar_conversao(anos, meses, dias)
        print(f" Verificação: {dias_verificacao} dias (diferença: {abs(total_dias - dias_verificacao)})")
        # marcos de vida
        marcos(total_dias)
    except ValueError:
        print("Por favor, digite apenas números inteiros!")

def verificar_conversao(anos, meses, dias):
    # Verificando a conversão
    total_dias = 0
    ano_atual = 2025


    # Somando dias dos anos completos
    for i in range(meses):
        ano_calculado = ano_atual - anos + i 
        if e_bissexto(ano_calculado):
            total_dias += 366
        else:
            total_dias += 365
    # Somar dias dos meses completos
    for i in range(meses):
        mes_calculado = i + 1
        ano_mes = ano_atual - anos
        total_dias += dias_no_mes(mes_calculado, ano_mes)
    # Somar os dias restantes 
    total_dias += dias 
    return total_dias

def marcos(total_dias):
    # Já perdi muito tempo nessa questão então estou fazendo coisas extra por nenhum motivo 
    print (f"\nMarcos Importantes:")

    marcos = [
        (365, "1 ano"),
        (365 * 5, "5 anos"),
        (365 * 10, "10 anos"),
        (365 * 18, "18 anos"),
        (365 * 21, "21 anos"),
        (365 * 30, "30 anos"),
        (365 * 50, "50 anos"),
        (365 * 65, "65 anos"),
        (365 * 100, "100 anos"),
    ]

    for dias_marco, descricao in marcos:
        if total_dias >= dias_marco:
            print(f"Já passou dos {descricao}")

        else: 
            dias_faltam = dias_marco - total_dias
            print(f"Faltam {dias_faltam} dias para {descricao}")
            break

# Função para testar como exemplos, na produção de código servia para testes
def teste_exemplos():
    print("\n--- Testes como Exemplos ---")
    exemplos = [
        365, #1ano
        730, #2anos
        1095, #3anos
        10000, #~27anos
        7300, #20anos
        18250 #50anos
    ]
    for dias in exemplos:
        anos, meses, dias_restantes = dias_para_idade(dias)
        print(f"{dias} dias = {anos} anos, {meses} meses, {dias_restantes} dias")

if __name__ == "__main__":
    main()
    teste_exemplos()