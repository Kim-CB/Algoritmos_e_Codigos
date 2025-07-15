def calcular_total():

    tabela_produtos = {
        1001: 5.32,
        1324: 6.45,
        6548: 2.37,
        987: 5.32,
        7623: 6.45
    }

    print("-- PREÇO TOTAL --")
    print()
    print("Produtos disponíveis:" , list(tabela_produtos.keys()))
    print()

    try:
        codigo = int(input("Digite o código do produto: "))

        if codigo not in tabela_produtos:
            print(f"Erro: Código {codigo} não encontrado na tabela de produtos.")
            print("Códigos válidos:", list(tabela_produtos.keys()))
            return
        
        quantidade = int(input("Qual a quantidade comprada? "))

        if quantidade <= 0:
            print("Erro: A quantidade deve ser um número posistivo.")
            return
        
        preco_unitario = tabela_produtos[codigo]
        preco_total = preco_unitario * quantidade

        print(f"--- RESULTADO DA COMPRA ---")
        print(f"Código do produto: {codigo}")
        print(f"Preço unitário: R$ {preco_unitario:.2f}")
        print(f"Quantidade: {quantidade}")
        print(f"Cálculo: R$ {preco_unitario:.2f} x {quantidade} = R$ {preco_total:.2f}")
        print(f"Preço total: R$ {preco_total:.2f}")

        print(f"\n--- EXTRAS ---")
        if quantidade > 10:
            print("Compra em grande quantidade.")
        if preco_total > 50:
            print("Compra em alto valor.")

        print(f"Valor médio por item: R$ {preco_total/quantidade:.2f}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

    except Exception as e: 
        print(f"Erro inesperado: {e}")

def multiplas_compras():
    tabela_produtos = {
        1001: 5.32,
        1324: 6.45,
        6548: 2.37,
        987: 5.32,
        7623: 6.45
    }

    print('--- MÚLTIPLAS COMPRAS ---')

    compras = []
    total_geral = 0

    while True:
        try:
            print(f"\n--- Compra {len(compras) + 1} ---")
            codigo = int(input("Digite o código do produto (0 para finalizar):"))

            if codigo == 0:
                break

            if codigo not in tabela_produtos:
                print(f"Código {codigo} não encontrado. Tente novamente.")
                continue

            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("Quantidade deve ser positiva. Tente novamente.")
                continue

            preco_unitario = tabela_produtos[codigo]
            preco_total = preco_unitario * quantidade

            compras.append({
                'codigo':codigo,
                'quantidade': quantidade,
                'preco_unitario': preco_unitario,
                'preco_total': preco_total
            })

            total_geral += preco_total

            print(f"Adicionado: {quantidade} x produto {codigo} = R$ {preco_total:.2f}")

        except ValueError:
            print("Erro: Digite apenas números válidos.")
    
    if compras:
        print(f"--- RESUMO FINAL ---")