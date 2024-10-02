import random

print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')
print()

print('CATEGORIAS:')
print('[1] FRUTAS')
print('[2] VEÍCULOS')
print('[3] NOMES PRÓPRIOS')
print()
escolha = int(input('Digite o número da categoria escolhida:'))


frutas = ['abacate', 'abacaxi', 'banana', 'caqui', 'coco', 'figo', 'goiaba', 'laranja', 'limao', 'mamao', 'manga', 'maracuja', 'marmelo', 'melancia', 'melao', 'pera', 'pessego', 'tangerina', 'uva']
veiculos = ['aviao', 'moto', 'carro', 'barco', 'bicicleta', 'patins', 'skate', 'triciculo']
nomes = ['ana', 'estevao', 'itamar', 'ricardo', 'rodrigo', 'bruno', 'victor', 'fabiana', 'vinicius', 'thiago', 'guilherme', 'bernardo', 'amanda', 'gabriela']

if escolha == 1:
    palavra_secreta = random.choice(frutas)
    categoria = 'Frutas'
if escolha == 2:
    palavra_secreta = random.choice(veiculos)
    categoria = 'Veículos'
if escolha == 3:
    palavra_secreta = random.choice(nomes)
    categoria = 'Nomes Próprios'

letras_acertadas = []

posicao = 0
for letra in palavra_secreta:
    letras_acertadas.append(letra)
    letras_acertadas[posicao] = '_'
    posicao += 1


acertou = False
enforcou = False
vidas = 6
print('-'*30)
print(f'Você escolheu a categoria "{categoria}"!')
print(f'Adivinhe a palavra secreta: "{letras_acertadas}"!')
print(f'Dica: a palavra tem {len(letras_acertadas)} letras!')
print('-'*30)
print()
while(not acertou and not enforcou):
    chute = input('Qual letra? ')
    print('-'*30)
    if (chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f'Encontrei a letra {letra} na posição {posicao}')
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        vidas -= 1
        print(f'A letra "{chute.upper()}" não faz parte da palavra secreta!')
        print(f'Você ainda tem {vidas} vidas restantes!')
        print()
    acertou = '_' not in letras_acertadas
    enforcou = vidas == 0
    print(letras_acertadas)

if acertou:
    print('-'*30)
    print(f'Parabéns! Você ganhou com {vidas} restantes!')
    print('-'*30)
else:
    print('-'*30)
    print('GAME OVER')
    print('Você Perdeu!')
    print(f'A palavra secreta era "{palavra_secreta}"')
    print('-'*30)

print('Fim do jogo')