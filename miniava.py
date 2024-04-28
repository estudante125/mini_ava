class Pessoa: # todos os objetos tem em comum um nome, email e telefone
    def init(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def str(self): # # O método __str personaliza a representação em string do objeto, tornando-a legível ao imprimir.
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"


class Reitor(Pessoa): # criando a class reitor que herda a classe pai pessoa
    def init(self, nome, email, telefone, id_reitor, salario):
        super().init(nome, email, telefone)
        self.id_reitor = id_reitor # quando chamada minha classe espera receber essas informações
        self.salario = salario # outra informação que minha classe espera receber ao ser chamada

    def str(self):
        return super().str() + f", ID do Reitor: {self.id_reitor}, Salário: {self.salario}"


class Estudante(Pessoa): # criando a class estudante que vai herdar a classe pessoa
    def init(self, nome, email, telefone, matricula, curso):
        super().init(nome, email, telefone)
        self.matricula = matricula
        self.curso = curso

    def str(self):
        return super().str() + f", Matrícula: {self.matricula}, Curso: {self.curso}"


class Professor(Pessoa):
    def init(self, nome, email, telefone, disciplina, id_professor, salario):
        super().init(nome, email, telefone)
        self.disciplina = disciplina
        self.id_professor = id_professor
        self.salario = salario

    def str(self):
        return super().str() + f", Disciplina: {self.disciplina}, ID do Professor: {self.id_professor}, Salário: {self.salario}"


def cadastrar_pessoa(): #criando a função para cadastrar pessoas
    tipo_pessoa = input("Digite o tipo de pessoa a ser cadastrada (reitor/estudante/professor): ").lower()

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = int(input("Telefone: "))

    if tipo_pessoa == 'reitor':
        id_reitor = input("ID do Reitor: ")
        salario = float(input("Salário do Reitor: "))
        pessoa = Reitor(nome, email, telefone, salario)
    elif tipo_pessoa == 'estudante':
        matricula = input("Matrícula do Estudante: ")
        curso = input("Curso do Estudante: ")
        pessoa = Estudante(nome, email, telefone, curso)
    elif tipo_pessoa == 'professor':
        disciplina = input("Disciplina do Professor: ")
        id_professor = input("ID do Professor: ")
        salario = float(input("Salário do Professor: "))
        pessoa = Professor(nome, email, telefone, disciplina, salario)
    else:
        print("Tipo de pessoa inválido.")
        return

    return pessoa


def main():
    pessoas = []

    while True:
        print("\nSistema de Cadastro mini ava")
        print("1. Cadastrar Pessoa")
        print("2. Visualizar Pessoas Cadastradas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pessoa = cadastrar_pessoa()
            if pessoa:
                pessoas.append(pessoa)
                print("Pessoa cadastrada com sucesso!")
        elif opcao == '2':
            if pessoas:
                print("\nInformações das pessoas cadastradas:")
                for pessoa in pessoas:
                    print(pessoa)
            else:
                print("Não há pessoas cadastradas.")
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()