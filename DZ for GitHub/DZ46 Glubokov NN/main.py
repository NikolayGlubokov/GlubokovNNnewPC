import os
from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.intruder import Intruder
from models.cars import Cars

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Cars).count())
    # print(session.query(Intruder).first())

    # for it in session.query(Intruder).filter(and_(Intruder.age >= 25, Intruder.id_car >=20)):
    #     print(it)
    #
    # for it in session.query(Cars).filter(and_(Cars.car_power>=400, Cars.car_model.like('Nissan%'))):
    #     print(it)
    #
    # print(session.query(Cars).filter(Cars.car_model.notin_(['Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus'])).all())

    # print(session.query(Cars).filter(Cars.car_model.in_(['Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus'])).all())
    #
    # for it in session.query(Intruder).order_by(Intruder.name):
    #     print(it)

    # for it in session.query(Cars).join(Intruder).filter(and_(Cars.car_model.like('Nissan%'), Intruder.id>20)):
    #     print(it)

    # i = session.query(Cars).get(7)
    # print(i)
    # i.car_power=500
    # print(i)
    # session.add(i)
    # session.commit()

    # session.add(Cars(id=59, car_model='Lamorghini Gallardo', car_power=700))
    # for it in session.query(Cars):
    #     print(it)
    # session.commit()

    s=session.query(Cars).filter(Cars.id==57).all()

    session.delete(s[0])

    session.commit()
    for it in session.query(Cars):
        print(it)
