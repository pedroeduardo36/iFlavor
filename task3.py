#ex.1

numeros_ate_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Pedro', 'Paulo', 'Robert', 'John']
ano_nascimento_e_atual = [2001, 2024]

#ex.2
for nome in nomes:
    print(nome)

#ex.3
soma_impares = 0
for i in range(1, 11, 2): #range -> O primeiro argumento é de onde começa, o segundo onde termina e o terceiro de quanto quanto ele conta
    soma_impares += i
print(soma_impares)

#ex.4
for i in range(1, 10, -1):
    print(i)

#ex.5
numero_tabuada = int(input('Insira um número para tabuada'))
for i in range(1, 11):
    print(numero_tabuada * i)       

#ex.6
soma = 0

try:
    for numero in numeros_ate_10:
        soma += numero
        print(f'Soma dos números: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

#ex.7
media = 0
soma_media = 0

try:
    for numero in numeros_ate_10:
        soma_media += numero
        media = soma_media / len(numeros_ate_10)
        print(f'Média dos números: {media}')
except ZeroDivisionError:
    print('A lista está vazia')
except Exception as e:
    print(f'Ocorreu um erro: {e}')