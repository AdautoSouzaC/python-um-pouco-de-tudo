#sintaxe:
#print(objetos, argumentos)

#Exemplo 1
nome = "Adauto Souza"
profissao = "Programador python e estudande de ciencia da computação,"
print (profissao, nome)

#Exemplo 2
nome = input("Qual o seu nome?:")
mensagem = ' Olá '  + nome + ' Seja bem vindo a empresa !'
print(mensagem)

#Exemplo 3
print("Imprima algo nessa linha")
print("imprimindo na linha abaixo, e ", end='')
print("seguindo na mesma linha")

#Exemplo 4 
nome = "Cristiane"
idade = 45
mensagem_formatada = "O nome dela é {0} e ela tem {1} anos".format(nome, idade)
print(mensagem_formatada)

Exemplo 5

nome = "Enzo"
peso = 65.00
print(f"Olá meu nome é {nome} e eu peso {peso} quilos")