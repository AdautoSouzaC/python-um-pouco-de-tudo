for contiex in range(1,6):
    print(f'\nRodada: {contiex}')
    for contin in range(5,0, -1):
        print(f'valor:{contin}')

print("Fim da contagem")

# Outro exemplo:

import random

for A in range(1,6):
    print(f"\nConjunto {A}")
    for b in range(5):
        num = random.randint(1,100)
        print(f'valor: {num}')