# https://docs.python.org/3/library/functions.html#open 
import os

file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('#'*30)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close() 

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

with open('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

os.remove('abc.txt')