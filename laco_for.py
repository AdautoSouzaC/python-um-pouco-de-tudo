lista = [2,4,8,9,7,1,3]
for i in  lista:
    print(lista)

# # Outro exemplo

lista = [2,4,8,9,7,1,3]
palavra = "Programacao"
for letra in  palavra:
    print(letra)

# Outro...

for numero in range(0,11):
    print(numero)

# Mais um...

nome = input("Digite seu nome: ")
for x in range(10):
    print(f'{x+1} {nome}')

# Range ( Valor incial, valor final e tambem incremento)

#  # Os exemploso seguem...

for i in range (2,20,2):
    print(i)
# # Laço conta de dois em dois até chegar no "20" a partir do 2
    
# # Exemplo com tuplas
    
pedras = ('rubi', 'esmeralda', 'quatzo', 'safira', 'diamante', 'turmalina')

for pedra in pedras:
    if pedra =='quatzo':
        continue
    print(pedra)