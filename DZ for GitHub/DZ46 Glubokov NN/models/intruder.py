from sqlalchemy import Column, ForeignKey, Integer, String

from models.database import Base


class Intruder(Base):
    __tablename__ = 'intruder'

    id = Column(Integer, nullable=False, primary_key=True)
    surname = Column(String(200), nullable=False)
    name = Column(String(200), nullable=False)
    age = Column(Integer, nullable=False)
    id_car = Column(Integer, ForeignKey('cars.id'))

    def __init__(self, full_name, age, id_car):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.age = age
        self.id_car = id_car

    def __repr__(self):
        return f'Black list: №{self.id}: {self.surname} {self.name}, {self.age} years old. ID CAR = {self.id_car}'
