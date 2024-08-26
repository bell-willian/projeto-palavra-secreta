import os

palavra_secreta = input('Digite uma palavra secreta: ')
letras_acertada = ''
tentativas = 0
while True:
    palavra_digitada = input('Digite apenas uma palavra: ')
    tentativas += 1
    if len(palavra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    if palavra_digitada in palavra_secreta:
        letras_acertada += palavra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada é {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas:{tentativas}')
        break