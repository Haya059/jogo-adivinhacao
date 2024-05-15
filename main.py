import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    
    while tentativas < max_tentativas:
        palpite = int(input('Digite seu palpite: '))
        tentativas += 1

        if palpite < numero_secreto:
            print('Errou! O número é mais alto')
        elif palpite > numero_secreto:
            print('Errou! O número é mais baixo')
        else:
            print(f'Parabéns! Você adivinhou o número em {tentativas} tentativas')
            break
    else:
        print(f'Poxa, você não conseguiu descobrir o número em 10 tentativas. O número era {numero_secreto}')
        return

print('Boas vindas ao Jogo da Adivinhação')
print('Tente adivinhar o número entre 1 e 100')


if __name__ == "__main__":
    jogo_adivinhacao()