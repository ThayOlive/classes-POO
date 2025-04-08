from datetime import datetime
import time

class Pet:
    def __init__(self,**kwargs):
        self.nome = kwargs.get('nome')
        self.idade = kwargs.get('idade')
        self.raça = kwargs.get('raça')
        self.especie = kwargs.get('especie')
        self.descricao = kwargs.get('descricao')
        self.horario = kwargs.get('horario')
        self.historico = kwargs.get('historico')
    
    def pet_info(self):
            return print(f'Nome:{self.nome} |Idade:{self.idade} |Raça: {self.raça} |Especie:{self.especie} |Descrição: {self.descricao} ')

    def consultar_agendamento(self):
        horario = self.horario.strftime("%Y-%m-%d %H:%M")
        return f'{self.nome} está agendado para {horario}'
    
    def alterar_agendamento(self, novo_horario):
        self.horario = novo_horario
    
    def adicionar_visita(self, descricao):
         self.historico.append(descricao)


pets = []

def menu():
     print("\n🐾 MENU - CLÍNICA PET 🐾")
     print("1 - Cadastrar Novo Pet")
     print("2 - Consultar agendamentos")
     print("3 - Listar pets")
     print("4 - Adcionar visita ao histórico")
     print("5 - Consultar histórico de um pet")
     print("0 - sair")

while True:
    time.sleep(0.10)
    menu()
    opcao = input("Escolha uma opção:")

    if opcao == '1':
         nome = input("Nome do pet:")
         idade = input("idade do pet:")
         raça = input("Raça do pet:")
         especie = input("Especie do pet:")
         descricao = input("Descricao:")
         data_str = input("Data do agendamento (formato: DD/MM/AAAA HH:MM): ")
         horario = datetime.strptime(data_str, "%d/%m/%Y %H:%M")  

         pet = Pet(nome=nome, idade= idade, raça= raça, especie= especie, descricao= descricao, horario= horario)
         pets.append(pet)

    elif opcao == '2':
        if not pets:
            print("Nenhum pet encontrado.")
        else:
            for pet in pets:
                print(pet.consultar_agendamento())

    elif opcao == '3':
        if not pets:
              print("Não tem pets cadastrados")
        
        for pet in pets:
            print(Pet.pet_info(pet))

    elif opcao == '4':
        nome_pet = input("Digite o nome do pet:")
        for pet in pets:
            if pet.nome.lower() == nome_pet.lower():
                desc = input("descrição da visita:")
                pet.adicionar_visita(desc)
                print("Visita adcionada!")
                break
        else:
             print("pet não encontrado.")

    elif opcao == '5':
        nome_pet = input("Digite o nome do pet:")
        for pet in pets:
            if pet.nome.lower() == nome_pet.lower():
                print(f'Histórico de{pet.nome}: {pet.historico}')
                break
        else:
          print("pet não encontrado.")

    elif opcao == '0':
        print("Até mais! Obrigada por usar a CLÍNICA PET")
    
    else:
        print("Opção inválida!")





         



pet1 = Pet(
    nome='Princesa',
    idade=13,
    raca='Poodle',
    especie='Cachorro',
    descricao='Muito dócil e carinhosa',
    horario=datetime(2025, 4, 12, 14, 0)
)

pet2 = Pet(
    nome='Thor',
    idade=5,
    raca='Labrador',
    especie='Cachorro',
    descricao='Ativo e brincalhão',
    horario=datetime(2025, 4, 13, 10, 30)
)

pet3 = Pet(
    nome='Mimi',
    idade=2,
    raca='Persa',
    especie='Gato',
    descricao='Gosta de dormir o dia todo',
    horario=datetime(2025, 4, 15, 9, 45)
)

pet4 = Pet(
    nome='Tico',
    idade=1,
    raca='Calopsita',
    especie='Ave',
    descricao='Muito falante e adora cantar',
    horario=datetime(2025, 4, 16, 11, 15)
)

pet5 = Pet(
    nome='Bidu',
    idade=7,
    raca='Vira-lata',
    especie='Cachorro',
    descricao='Muito esperto e amigável',
    horario=datetime(2025, 4, 17, 13, 0)
)

novo_horario = datetime(2025, 4, 17, 14, 0)
pet5.alterar_agendamento(novo_horario)
print(Pet.consultar_agendamento(pet5))



