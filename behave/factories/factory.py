from faker import Faker
import random

fake = Faker('pt_BR')
class Revista:
    data = {}

    def __init__(self):
        self.data.update({
            'Codigo de Barras': random.randint(100,100000),
            'Titulo da revista:': fake.text(max_nb_chars=50),
            'Numero de paginas:': random.randint(1,100),
            'Data da publicacao:': fake.date(pattern="%Y-%m-%d"),
            'Quantidade em estoque:': random.randint(1,20),
        })

    def __str__(self):
        return "{}x Revista {} com {} paginas ".format(self.data['Qtde'], self.data['Titulo'], self.data['Pagina'])

    def __repr__(self):
        return "Revista({})".format(str(self.data))