class Aluno:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"O(A) aluno(a) {self.nome}, com a matrícula nº{self.matricula} está matriculado(a) na {self.escola}"

def mostrar_alunos(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Aluno("Marcos", 1)
aluno_2 = Aluno("Thais", 2)

mostrar_alunos(aluno_1, aluno_2)

Aluno.escola = "Python"

aluno_3 = Aluno("Celia", 3)

mostrar_alunos(aluno_1, aluno_2, aluno_3)