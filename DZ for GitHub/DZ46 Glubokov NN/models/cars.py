from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    car_model = Column(String(200), nullable=False)
    car_power = Column(Integer)


    def __repr__(self):
        return f'ID car {self.id}: {self.car_model} - {self.car_power} HP'
