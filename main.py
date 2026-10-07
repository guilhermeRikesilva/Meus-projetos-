try:
    from SistemaChamados import SistemaChamados
except ImportError:
    from sistema_chamados import SistemaChamados

sistema = SistemaChamados()

def exibir_menu():
    print("\n========================")
    print("    SISTEMA DE CHAMADOS")
    print("=======================")
    print("1 - Abrir chamado")
    print("2 - Listar chamados")
    print("3 - Buscar chamado")
    print("4 - Alterar status")
    print("5 - Fechar chamado")
    print("0 - Sair")
while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")
    if opcao == "1":
        print("\n=== ABRIR CHAMADO ===")
        solicitante = input ("Solicitante: ")
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        sistema.abrir_chamado(solicitante, titulo, descricao)
    
    elif opcao == "2":
        sistema.listar_chamados()
    elif opcao == "3":
        try:
            id_chamado = int (
                input("\nInforme o ID do chamado:")
            )
            chamado = sistema.buscar_chamado(id_chamado)
            if chamado:
                chamado.exibir()
            else:
                print("\nChamado não encontrado.")
        except ValueError:
            print("\ndigite u mID válido. ")
    elif opcao == "4":
        try:
            id_chamado = int(input("\nInforme o ID do chamado: "))
            print("\n1 - ABERTO")
            print("2 - EM ANDAMENTo")
            print("3 - FECHADO")
            status = input("Novo status: ")
            if status == "1":
                novo_status = "ABERTO"
            elif status == "2":
                novo_status = "EM ANDAMENTO"
            elif status == "3":
                novo_status = "FECHADO"
            else:
                print("Status inválido. ")
                continue
            sistema.alterar_status(id_chamado, novo_status)
        except ValueError:
            print("\nDigite um ID válido.")
    elif opcao == "5":
        try:
            id_chamado = int(input("\nInforme o ID do chamado: "))
            sistema.fechar_chamado(id_chamado)
        except ValueError:
            print("\nDigite um ID válido.")
    elif opcao == "0":
        print("\nSistema encerrado. ")
        break
    else:
        print("\nOpção inválida. ")
