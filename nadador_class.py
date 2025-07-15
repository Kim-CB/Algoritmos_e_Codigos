def classificar_nadador(idade):
    # Classificar um nadador com base na idade
    if idade < 5:
        raise ValueError("Idade muito baixa para competição!")
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    if idade > 120:
        raise ValueError("Senhor se você nadar, vai morrer do coração e me dar trabalho.")
    
    # Classificação categoria
    if 5 <= idade <= 7:
        return {
            'categoria': 'Infatil A',
            'faixa_etaria': '5-7 anos',
            'codigo': 'INF_A',
            'descricao': 'Categoria iniciante para crianças'
        }
    elif 8 <= idade <= 10:
        return {
            'categoria': 'Infatil B',
            'faixa_etaria': '8-10 anos',
            'codigo': 'INF_B',
            'descricao': 'Categoria infantil intermediária'
        }
    elif 11 <= idade <= 13:
        return {
            'categoria': 'Juvenil A',
            'faixa_etaria': '11-13 anos',
            'codigo': 'JUV_A',
            'descricao': 'Categoria juvenil inicial'
        }
    elif 14 <= idade <= 17:
        return {
            'categoria': 'Juvenil B',
            'faixa_etaria': '14-17 anos',
            'codigo': 'JUV_B',
            'descricao': 'Categoria juvenil avançada'
        }
    elif idade >= 18:
        return {
            'categoria': 'Adulto',
            'faixa_etaria': '18+ anos',
            'codigo': 'ADULTO',
            'descricao': 'Categoria adulta'
        }
    else:
        raise ValueError("Idade inválida para classificação!")
    
def caract_categorias(categoria_info):
    # Caracteristicas específicas 

    categoria = categoria_info['codigo']
    
    caracteristicas = {
        'INF_A': {
            'distancias_comuns': ['25m', '50m'],
            'estilos_recomendados': ['Livre', 'Costas'],
            'observacoes': 'Foco na adaptação à água',
            'tempo_prova': '15-20 minutos',
            'supervisao': 'Supervisão constante'
        },
        'INF_B': {
            'distancias_comuns': ['25m', '50m', '100m'],
            'estilos_recomendados': ['Livre', 'Costas', 'Peito'],
            'observacoes': 'Desenvolvimento de técnicas básicas',
            'tempo_prova': '30-45 minutos',
            'supervisao': 'Supervisão recomendada'
        },
        'JUV_A': {
            'distancias_comuns': ['50m', '100m', '200m'],
            'estilos_recomendados': ['Livre', 'Costas', 'Peito', 'Borboleta'],
            'observacoes': 'Aperfeiçoamento técnico e resistência',
            'tempo_prova': '45-60 minutos',
            'supervisao': 'Supervisão moderada'
        },
        'JUV_B': {
            'distancias_comuns': ['100m', '200m', '400m'],
            'estilos_recomendados': ['Todos os estilos', 'Medley'],
            'observacoes': 'Competição mais pegada e especialização',
            'tempo_prova': '60-90 minutos',
            'supervisao': 'Supervisão básica'
        },
        'ADULTO': {
            'distancias_comuns': ['100M', '200m', '400m', '800m', '1500m'],
            'estilos_recomendados': ['Todos os estilos', 'Medley', 'Águas abertas'],
            'observacoes': 'Todas as modalidades disponíveis',
            'tempo_prova': '90+ minutos',
            'supervisao': 'Autonomia completa'
        }
    }
    return caracteristicas.get(categoria, {})

def main():

    print("--- Classificador de Nadadores por Idade --- ")
    print("Sistema de classificação para competições de natação")
    print("\nCategorias disponíveis:")
    print("- Infantil A: 5-7 anos")
    print("- Infantil B: 8-10 anos")
    print("- Juvenil A: 11-13 anos")
    print("- Juvenil B: 14-17 anos")
    print("- Adulto: 18+ anos")

    try: 
        idade = int(input("\nDigite a idade do nadador: "))

        resultado = classificar_nadador(idade)
        caracteristicas = caract_categorias(resultado)

        print("\n------------------------")
        print("RESULTADO DA CLASSIFICAÇÃO")
        print("\n------------------------")
        print(f"Idade: {idade} anos")
        print(f"Categoria: {resultado['categoria']}")
        print(f"Faixa etária: {resultado['faixa_etaria']}")
        print(f"Código: {resultado['codigo']}")
        print(f"Descrição: {resultado['descricao']}")

        if caracteristicas:
            print("\n------------------------")
            print("CATEGORIA")
            print("\n------------------------")
            print(f"Distâncias comuns: {', '. join(caracteristicas['distancias_comuns'])}")
            print(f"Estilos recomendados: {', '.join(caracteristicas['estilos_recomendados'])}")
            print(f"Observações: {caracteristicas['observacoes']}")
            print(f"Tempo típico de prova: {caracteristicas['tempo_prova']}")
            print(f"Supervisão {caracteristicas['supervisao']}")
        
        
    except ValueError as e:
        print(f"\nErro: {e}")
        print("Por favor, digite uma idade válida!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def testes():
        print("--------------------------")
        print("TESTES")
        print("--------------------------")

        idade_teste = [5, 7, 8, 10, 11, 13, 17, 18, 45, 3, 121]

        for idade in idade_teste:
            print(f"\nTeste - Idade: {idade} anos")
            print("--------------------------")

            try: 
                resultado = classificar_nadador(idade)
                print(f"Categoria: {resultado['categoria']} ({resultado['faixa_etaria']})")
                print(f"Descrição: {resultado['descricao']}")
            except ValueError as e:
                print(f"Erro: {e}")



def menu():

    while True:
        print("--------------------------")
        print("CLASSIFICAÇÃO NADADORES")
        print("--------------------------")
        print("1. Classificar um nadador")
        print("2. Executar testes automáticos com idade pré-definidas")
        print("3. Sair")
        print("--------------------------")

        try:
            opcao = int(input("Escolha uma opção (1-3):"))

            if opcao == 1:
                main()
            elif opcao == 2:
                testes()
            elif opcao == 3:
                print("Obrigado por usar o Sistema de Classificação de Nadadores!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 3.")
        except ValueError:
            print("Por favor, digite apenas números!")

if __name__ == "__main__":
    menu()