import mod_func as mf

if __name__ == '__main__':
    mf.mensagem()
    num = int(input('Digitr um numrero inteiro:'))
    
    print(f'\nCalcular fatorial do numero:')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')


    print(f'\nCalcular seuquencia de fibonacci:')
    fib = mf.fibo(num)
    print(f'O fatorial é {fib}')