    if __name__ == '__main__':
        av1 = float(input('Digite a nota da primeira avaliação: '))
        av2 = float(input('Digite a nota da segunda avaliação: '))
        p1 = 3.5 * av1
        p2 = 7.5 * av2
        media = (p1 + p2) / 11
        print('MÉDIA = {:.5f}'.format(media))
