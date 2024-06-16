#A primeira parte desse código define a funcionalidade do programa com os objetos e funções, tudo depois de "while True" na linha 53 é para permitir a interação com o código pelo terminal do computador

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livrosRegistrados = []
    
    def Registrar(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livrosRegistrados.append(livro)
        print("O livro foi registrado!")
    
    def Emprestar(self, titulo):
        for livro in self.livrosRegistrados:
            if (livro.titulo == titulo):
                if livro.disponivel:
                    livro.disponivel = False
                    print("O livro foi emprestado, obrigado!")
                    return
                else:
                    print("O livro nao esta disponivel :(")
                    return
        print("O livro nao foi encontrado :( ")

    def Devolver(self, titulo):
        for livro in self.livrosRegistrados:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    livro.disponivel = True
                    print("Voce devolveu o livro! Obrigado!")
                    return
                else:
                    print("O livro ja esta disponivel!")
                    return
        print("O livro nao foi encontrado :(")

    def Listar(self):
        print("Livros disponíveis:")
        for livro in self.livrosRegistrados:
            if livro.disponivel:
                print(f"{livro.titulo} por {livro.autor}")

Pyblioteca = Biblioteca()

if __name__ == "__main__":
    print("Bem vindo a Pyblioteca!\n Para ver a lista de livros disponíveis, use 'Listar' \n Para registrar um livro, use 'Registrar' \n Para emprestar um livro, use 'Emprestar' \n Para devolver um livro, use 'Devolver' \nBoa leitura!")

while True:
        comando = input("Digite o comando: ").lower()
        if comando == "listar":
            Pyblioteca.Listar()
        elif comando.startswith("registrar "):
            try:
                _, titulo, autor = comando.split(" ", 2)
                Pyblioteca.Registrar(titulo, autor)
            except ValueError:
                print("Por favor, use 'registrar <titulo> <autor>'")
        elif comando.startswith("emprestar "):
            try:
                _, titulo = comando.split(" ", 1)
                Pyblioteca.Emprestar(titulo)
            except ValueError:
                print("Por favor, use 'emprestar <titulo>'")
        elif comando.startswith("devolver "):
            try:
                _, titulo = comando.split(" ", 1)
                Pyblioteca.Devolver(titulo)
            except ValueError:
                print("Por favor, use 'devolver <titulo>'")
        else:
            print("Desculpe, o comando nao foi entendido :( ")