import json

d1 = {
    'Pessoa 1': {
        'nome': 'Gustavo',
        'idade': 28,
    },
    'Pessoa 2': {
        'nome': 'Bernardo',
        'idade': 3,
    },
}

d1Json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1Json)

