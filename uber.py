from pathlib import Path

colaboradores = [
    {
        "nome": "ana carolina",
        "endereco": "rua das flores, 120",
        "telefone": "11987654321"
    },
    {
        "nome": "bruno henrique lima",
        "endereco": "avenida central, 45",
        "telefone": "11976543210"
    },
    {
        "nome": "carla fernanda rocha",
        "endereco": "rua do bosque, 78",
        "telefone": "11965432109"
    },
    {
        "nome": "diego augusto mendes",
        "endereco": "rua são joão, 230",
        "telefone": "11954321098"
    },
    {
        "nome": "elisa cristina almeida",
        "endereco": "avenida brasil, 315",
        "telefone": "11943210987"
    },
    {
        "nome": "felipe gabriel santos",
        "endereco": "rua das palmeiras, 64",
        "telefone": "11932109876"
    }
]

print("Solicitação de Uber")
data = input("Data da hora extra: ")
quantidade = int(input("Quantos colaboradores virão: "))
hora_extra = []

while len(hora_extra) != quantidade:
    nome = input("nome do colaborador: ")
    for pessoa in colaboradores:
        if nome.lower() in pessoa['nome'].lower():
            hora_extra.append(pessoa)
            
def salvar_informacoes(lista, data):
    caminho = Path(__file__).parent / "pedidos.txt"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Bom dia!\n")
        arquivo.write(f"Segue abaixo a solicitação de Uber para o dia: {data}\n")
        arquivo.write("Solicitações\n\n")
        
        
        for pessoa in lista:
            arquivo.write(f"Data: {data}\n")
            arquivo.write(f"Colaborador: {pessoa['nome']}\n")
            arquivo.write(f"Telefone: {pessoa['telefone']}\n")
            arquivo.write(f"Partida: {pessoa['endereco']}\n")
            arquivo.write("Destino: Portaria 2\n")
            arquivo.write("Horário ida: 15:38 (estar na fábrica)\n")
            arquivo.write("Horário volta: 22:00\n")
            arquivo.write("Missão: \n")
            arquivo.write("--------------------------------\n")
        
salvar_informacoes(hora_extra, data)
