
if __name__ == '__main__':
    v = input('Digite três valores em sequência dando um espaço entre eles: ').split()
    a, b, c = int(v[0]), int(v[1]), int(v[2])
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    print('{} eh o maior'.format(maior))
