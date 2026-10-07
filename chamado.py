class Chamado:
    def __init__(self, id, solicitante, titulo, descricao):
        self.id = id
        self.solicitante = solicitante
        self.titulo = titulo
        self.descricao = descricao
        self.status = "ABERTO"
    def alterar_status(self, novo_status):
        self.status = novo_status
    def exibir(self):
        print("-" * 40)
        print(f"ID: {self.id}")
        print(f"Solicitante: {self.solicitante}")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Status: {self.status}")