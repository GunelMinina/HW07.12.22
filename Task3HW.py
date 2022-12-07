# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compress(path):
    txt = ''
    count = 0
    if len(path) == 1:
        txt += '1' + path[0]
        return txt
 
    for i in range(len(path)):
        count += 1
        if (i + 1) == len(path) or path[i] != path[i + 1]:
             txt += str(count) + path[i]
             count = 0
    return txt

def decompress(path):
    txt = ''
    i = 0
    while i <= len(path) - 2:
        for j in range(0, int(path[i])):
            txt += path[i+1]
        i += 2
    return txt

tocompress = open('tocompress.txt','r').read().splitlines()
compressed = list(map(compress, tocompress))

open('compressed.txt', 'w+').writelines((f"{l}\n" for l in compressed))

todecompress = open('todecompress.txt','r').read().splitlines()
decompressed = list(map(decompress, todecompress))

open('decompressed.txt', 'w+').writelines((f"{l}\n" for l in decompressed))