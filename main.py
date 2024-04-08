class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.emprestado = False

    def emprestar(self):
        self.emprestado = True

    def devolver(self):
        self.emprestado = False


class Membro:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.historico = []

    def emprestar_livro(self, livro):
        self.historico.append(livro)

    def devolver_livro(self, livro):
        if livro in self.historico:
            self.historico.remove(livro)


class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.id] = livro

    def adicionar_membro(self, membro):
        self.membros[membro.numero] = membro

    def emprestar_livro(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro and not livro.emprestado:
            livro.emprestar()
            membro.emprestar_livro(livro)
            print("Livro emprestado com sucesso.")
        else:
            print("Livro não disponível ou membro inválido.")

    def devolver_livro(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro and livro.emprestado:
            livro.devolver()
            membro.devolver_livro(livro)
            print("Livro devolvido com sucesso.")
        else:
            print("Livro não emprestado ou membro inválido.")

    def pesquisar_livro_por_titulo(self, titulo):
        for livro in self.catalogo.values():
            if livro.titulo == titulo:
                print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Disponível: {'Sim' if not livro.emprestado else 'Não'}")

    def pesquisar_livro_por_autor(self, autor):
        for livro in self.catalogo.values():
            if livro.autor == autor:
                print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Disponível: {'Sim' if not livro.emprestado else 'Não'}")

    def pesquisar_livro_por_id(self, id):
        livro = self.catalogo.get(id)
        if livro:
            print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Disponível: {'Sim' if not livro.emprestado else 'Não'}")
        else:
            print("Livro não encontrado.")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("A Metamorfose", "Franz Kafka", 1)
    livro2 = Livro("1984", "George Orwell", 2)

    membro1 = Membro("João", 123)
    membro2 = Membro("Maria", 456)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.adicionar_membro(membro1)
    biblioteca.adicionar_membro(membro2)

    biblioteca.emprestar_livro(1, 123)
    biblioteca.devolver_livro(1, 123)

    biblioteca.pesquisar_livro_por_autor("George Orwell")
