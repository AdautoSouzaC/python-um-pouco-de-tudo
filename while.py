numero = 1
while(numero <100):
    print(numero)
    numero += 1

print("Fim do laço")

#outro exemplo de while

texto = None

while True:
    print("Digite uma frase ou 'X' para parar:")
    texto = input() 
    if texto == 'x' or texto == "X":
        break

    print(f'seja bem vindo, você digitou: , {texto}')

print("Até mais")

    