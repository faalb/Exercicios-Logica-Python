if __name__ == '__main__':
    a = float(input('Digite a nota da avaliação 1: '))
    b = float(input('Digite a nota da avaliação 2: '))
    c = float(input('Digite a nota da avaliação 3: '))
    pa = 2 * a
    pb = 3 * b
    pc = 5 * c
    media = (pa + pb + pc) / 10
    print('MÉDIA = {}'.format(media))
