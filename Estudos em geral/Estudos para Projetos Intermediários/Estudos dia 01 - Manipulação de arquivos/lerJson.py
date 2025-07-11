import json

with open('abc.json', 'r') as file:
    d1Json = file.read()
    d1Json = json.loads(d1Json)

for k, v in d1Json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)