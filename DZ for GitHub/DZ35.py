import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    dct = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(nums)

    while len(dct) != 10:
        dct += choice(nums)

    person = {dct:{
        'name': name,
        'tel': tel}
    }
    return person


def write_json(personal_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = []

    data.append(personal_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())


def load_from_file():
    with open('persons.json', 'r') as f:
        print(json.load(f), indent=2)

load_from_file()
