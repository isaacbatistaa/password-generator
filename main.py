import random
import string

comprimento = int(input('Comprimento da senha: '))
print("Digite 's' para adicionar as opções abaixo.")

numeros = input('Numeros?')
minusculas = input('Minusculas?')
maiusculas = input('Maiusculas?')
caracteresespeciais = input('Caracteres especiais?')

caracteres = ''

if numeros == 's':
    caracteres += 'string.digits + '
if minusculas == 's':
    caracteres += 'string.ascii_lowercase + '
if maiusculas == 's':
    caracteres += 'string.ascii_uppercase + '
if caracteresespeciais == 's':
    caracteres += 'string.punctuation'

senha = ''.join(random.choice(eval(caracteres)) for _ in range(comprimento))
print('SUA SENHA É:', senha)
