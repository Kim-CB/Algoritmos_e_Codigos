

def contar_votos():
    print("-- Sistema de contagem de votos --")
    print()

    # Variáveis
    valor_totais = 0 # total de eleitores (denominador para percentual)
    branco = 0
    nulo = 0
    validos = 0
    candidatos = [] # Extra - Lista para armazenar votos dos candidatos

    while True:
        try:
            total_eleitores = int(input("Digite o número total de eleitores no município: "))
            if total_eleitores > 0:
                break
            else:
                print("O número de eleitores deve ser maior que zero!")
        except ValueError:
            print("Por favor, digite um número válido!")

    print(f"\nTotal de eleitores cadastrados: {total_eleitores}")
    print(f"\n-- CONTAGEM DE VOTOS --")
    print("Opções: ")
    print("1 - Voto em cadidato (digite o número do cadidato)")
    print("0 - Voto em branco")
    print("-1 - Voto nulo")
    print("999 - Finalizar contagem")
    print()

    while True:
        try:
            voto = input("Digite o voto (ou 999 para finalizar): ").strip()
            # Parar votação
            if voto == "999":
                break
            elif voto == "0":
                branco += 1
                valor_totais += 1
                print("Voto nulo registrado")
            else:
                numero_cadidato = int(voto)
                if numero_cadidato > 0:

                    cadidato_encontrado = False
                    for i, candidato in enumerate(candidatos):
                        if candidato['numero'] == numero_cadidato:
                            candidatos[i]['votos'] += 1
                            cadidato_encontrado = True
                            break

                    if not cadidato_encontrado:
                        candidatos.append({
                            'numero': numero_cadidato,
                            'votos': 1
                        })
                    validos += 1 
                    valor_totais += 1
                    print(f" Voto no candidato {numero_cadidato} registrado")
                else:
                    print(" Número de cadidato inválido! Use números positivos.")
        except ValueError:
            print(" Entrada inválida! Digite um número válido.")
        except KeyboardInterrupt:
            print("\n\nContagem interrompida pelo usuário.")
            break
    if valor_totais == 0:
        print("Nenhum voto foi registrado!")
        return
    
    # Calcular os percentuais
    perc_branco = (branco / total_eleitores ) * 100
    perc_nulo = (nulo / total_eleitores ) * 100
    perc_validos = (validos / total_eleitores ) * 100
    perc_abstencao = ((total_eleitores - valor_totais) / total_eleitores ) * 100
    perc_comparecimento = (valor_totais / total_eleitores) * 100

    # ordenando decrescente
    candidatos.sort(key=lambda x: x['votos'], reverse=True)

    # resultados
    print("\n-------------------------------------------------")
    print("RELATÓRIO FINAL DA ELEIÇÃO")
    print("----------------------------------------")

    print(f"\n RESUMO:")
    print(f"Total de eleitores no município: {total_eleitores}")
    print(f"Total de votos registrados: {valor_totais:,}")
    print(f"Abstenções: {total_eleitores - valor_totais:,}")
    print(f"Comparecimento: {perc_comparecimento:.2f} %")

    print(f"\n DISTRIBUIÇÃO DE VOTOS:")
    print(f"Votos válidos: {validos:,} ({perc_validos}% dos eleitores)")
    print(f"Votos em branco: {branco:,} ({perc_branco}% dos eleitores)")
    print(f"Votos nulos: {nulo:,} ({perc_nulo}% dos eleitores)")
    print(f"Abstenções: {total_eleitores - valor_totais:,} ({perc_abstencao}% dos eleitores)")

    if candidatos:
        print(f"\n RESULTADO POR CANDIDATO:")
        for i, candidato in enumerate(candidatos, 1):
            perc_candidato = (candidato['votos'] / total_eleitores) * 100
            perc_validos_candidato = (candidato['votos'] / validos) * 100 if validos > 0 else 0

            print(f"{i}º lugar - Candidato {candidato['numero']}: "
                  f"{candidato['votos']:,} votos"
                  f"({perc_candidato:.2f}% dos eleitores"
                  f"{perc_validos_candidato:.2f}% dos votos válidos)")
            
    print(f"\n VERIFICAÇÃO:")
    total_verificacao = validos + branco + nulo
    if total_verificacao == valor_totais:
        print("Contagem conferida - todos os votos foram contabilizados corretamente!")
    else: 
        print(" ERRO na contagem - verificar cálculos.")
    print(f"Total verificado: {total_verificacao} = {validos} + {branco} + {nulo}")

def exemplo():
    print("-- EXEMPLO DEMONSTRATIVO --")
    print("Simulando uma eleição com:")
    print("- 10.000 eleitores cadastrados")
    print("- 7.500 votos registrados")
    print()

    total_eleitores = 10000
    candidatos = [
        {'numero': 13, 'votos': 3500},
        {'numero': 22, 'votos': 2800},
        {'numero': 45, 'votos': 800}
    ]
    branco = 300
    nulo = 100
    validos = sum(c['votos'] for c in candidatos)
    valor_totais = validos + branco + nulo

    perc_branco = (branco / total_eleitores ) * 100
    perc_nulo = (nulo / total_eleitores ) * 100
    perc_validos = (validos / total_eleitores ) * 100
    perc_abstencao = ((total_eleitores - valor_totais) / total_eleitores ) * 100

    print(f"\n DISTRIBUIÇÃO DE VOTOS:")
    print(f"Votos válidos: {validos:,} ({perc_validos}% dos eleitores)")
    print(f"Votos em branco: {branco:,} ({perc_branco}% dos eleitores)")
    print(f"Votos nulos: {nulo:,} ({perc_nulo}% dos eleitores)")
    print(f"Abstenções: {total_eleitores - valor_totais:,} ({perc_abstencao}% dos eleitores)")

    print("\nCandidatos:")
    for candidato in candidatos:
        perc = (candidato['votos'] / total_eleitores) * 100
        print(f"Candidato {candidato['numero']}: {candidato['votos']:,} votos ({perc:.2f}%)")

if __name__ == "__main__":
    while True:    
        print("Escolha uma opção: ")
        print("1 - Executar sistema de contagem")
        print("2 - Ver exemplo demonstrativo")

        opcao = input("Digite sua escolha (1 ou 2):").strip()

        if opcao == "1":
            contar_votos()
        elif opcao == "2":
            exemplo()
        elif opcao == "3":
            print("-- TCHAU! --")
            break
        else:
            print("Opção inválida!")
