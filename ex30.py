if __name__ == '__main__':
    v = input('Digite dois valores iteiros: ').split()
    a, b = int(v[0]), int(v[1])

    if b % a == 0:
        print('São multiplos! ')
    else:
        print('Não são multiplos! ')
