if __name__ == '__main__':
    v = input('Digite dois valores separando-os com um espaço: ').split()
    x, y = float(v[0]), float(v[1])

    if x > 0 and y > 0:
        print('Os valores estão no primeiro quadrante! ')
    elif x < 0 and y > 0:
        print('Os valores estão no segundo quadrante! ')
    elif x < 0 and y < 0:
        print('Os valores estão no terceiro quadrante! ')
    elif x > 0 and y < 0:
        print('Os valores estão no quarto quadrante! ')
    elif x == 0 and y == 0:
        print('os valores estão na origem! ')
    elif x == 0 or y == 0:
        print('Um dos valores estão sobre um dos eixos! ')
