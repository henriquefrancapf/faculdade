def main():
    lista_compras = []

    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Exibir lista")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_item = input("Nome do item: ")
            categoria = input("Categoria do item: ")
            lista_compras.append((nome_item, categoria))
            print(f"Item '{nome_item}' adicionado.")

        elif opcao == '2':
            nome_item = input("Nome do item a remover: ")
            lista_compras = [item for item in lista_compras if item[0] != nome_item]
            print(f"Item '{nome_item}' removido.")

        elif opcao == '3':
            print("\nLista de Compras:")
            for item in lista_compras:
                print(f"{item[0]} - {item[1]}")
            if not lista_compras:
                print("A lista está vazia.")

        elif opcao == '4':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
