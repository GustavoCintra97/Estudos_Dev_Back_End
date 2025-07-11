import os

caminhoProcura = input(r'Digite o caminho: ')
termoProcura = input('Digite o termo: ')

def formataTamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.',',')

conta =0
for raiz, diretorios, arquivos in os.walk(caminhoProcura):
    for arquivo in arquivos:
        if termoProcura in arquivo:
            try:
                conta += 1
                caminhoCompleto = os.path.join(raiz, arquivo)
                nomeArquivo, extArquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminhoCompleto)
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)

            print()
            print('Encontrei o arquivo: ', arquivo)
            print('Caminho: ', caminhoCompleto)
            print('Nome: ', nomeArquivo)
            print('Extensão: ', extArquivo)
            print('Tamanho: ', formataTamanho(tamanho))

print()
print(f'{conta} encontrados')