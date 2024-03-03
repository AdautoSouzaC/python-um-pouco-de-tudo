#Gerando numeros aleatorios
import random

print("Gerar numeros aleatorios entre 1 e 50")
for i in range(5):
     n = random.randint(1,50)
     print(f'numerdo gerado {n}')

# Gereando 5 numeros aleatorios de 1 a 50

valor = random.random()
print(f'Número gerado: {round(valor * 10, 2)}')

valor = random.uniform(1, 100)
print(f'Numero: {round(valor, 4)}')
#Outro exemplo

lista = [4, 10, 17, 19, 29 ]
numero = random.choice(lista)
print(f'Numero escohido: {numero}')
numero = random.sample(lista,3)
print(f'Numeros escolhidos : {numero}')

#Embaralhar
print(f'Exibir lista original: {lista}')
print(f'Embaralhar lista e exibi - la')
numero = random.shuffle(lista)
print(lista)