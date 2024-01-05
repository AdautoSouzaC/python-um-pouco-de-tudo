idade = 26
altura = 1.83

resultado = (idade >=18) and (altura >=1.70)
mensagem = "Essa pessoa pode entar no evento?" + str (resultado)

print(mensagem)

#Programa de alarme

porta = "aberta"
janela = "aberta"

alarme  = (porta == 'aberta') or (janela == 'aberta')
mensagem = "Alarme disparado? " + str(alarme)
print(mensagem)

#Tem dinheiro

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro

mensagem = "Tem dinheiro "  + str(tem_dinheiro)
print(mensagem)