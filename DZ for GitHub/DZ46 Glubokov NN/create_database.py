from faker import Faker
import random

from models.database import create_db, Session
from models.intruder import Intruder
from models.cars import Cars



def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    n=int(input('Введите число нарушителей: '))
    car_list = [ 'Volkswagen Golf GTI', 'Honda Civic', 'Peugeot 206', 'Mazda MX-5','Dodge neon',
'Mitsubishi Motors Eclipse','Toyota Celica','Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus',
'Subaru Impreza', 'Hyundai Tiburon GT V6','Nissan Sentra SE R SPEC V','Nissan 240SX','Toyota Supra',
'Acura RSX','Acura Integra Type R', 'Nissan 350Z','Honda S2000', 'Nissan Skyline GTR']

    for i in range(n):
        car = Cars(id=i+1,car_model=random.choice(car_list), car_power=random.randint(300,700))
        session.add(car)

    faker = Faker('ru-Ru')

    for _ in range(n):
        full_name = faker.name().split()
        age=faker.random.randint(16,40)
        id_car = _+1
        intruder=Intruder(full_name, age, id_car)
        session.add(intruder)


    session.commit()
    session.close()
