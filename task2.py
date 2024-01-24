import os
#ex.1 
numero_inserido = int(input('Insira um número\n'))

if numero_inserido % 2 == 0:
    os.system('clear')
    print('\nO número inserido é par')
else:
    os.system('clear')
    print('\nO número inserido é impar')

#ex.2 
idade_usuario = int(input('Insira a sua idade \n'))

if idade_usuario <= 12:
    os.system('clear')
    print('Você é uma criança')
elif 12 < idade_usuario <= 18:
    os.system('clear')
    print('Você é um adolescence')
elif idade_usuario > 18: 
    os.system('clear')
    print('Você é adulto')
else: 
    os.system('clear')
    print('Valor inválido')

#ex.3 
user = 'Pedro'
password = '1234'

user_input = input('Username \n')
password_input = input('Password \n')

if user == user_input and password == password_input:
    os.system('clear')
    print('Acesso concedido')
else:
    os.system('clear')
    print('dados não conferem. Acesso negado')

#ex.4
x = int(input('Eixo X \n'))
y = int(input('Eixo Y \n'))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('Eixo | Origem')