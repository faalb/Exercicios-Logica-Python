if __name__ == '__main__':
    v = input('Digite três valores na mesma linha separando-os com um espaço: ').split()
    a, b, c = float(v[0]), float(v[1]), float(v[2])

    if a < (b+c) and b < (a+c) and c < (a+b):
        print('perímetro = {:.1f}'.format(a+b+c))
    else:
        print('Area = {:.1f}'.format((a+b)*c/2))
