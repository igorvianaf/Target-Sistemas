#tratamento de erro
try:
    #entrada de dado
    n = int(input('Informe um número: '))
    #primeiro e segundo termo da sequência
    t1 = 0
    t2 = 1
    #lista para armazenar termos
    n_fibonacci = [t1, t2]

#base para começar contagem a partir de terceiro termo
    cont = 3
    #loog para definir quantidade de termos criados
    while cont <= n:
        #regra da sequência
        t3 = t1 + t2
        #adicionar novo número a lista de termos
        n_fibonacci.append(t3)
        #redirecionar valores de t1, t2 e t3 para continuar a progressão de termos
        t1 = t2
        t2 = t3
        cont += 1
#desemcapsulamento de lista
    print(*n_fibonacci)
    #checar se o número pertence a sequência
    if n in n_fibonacci:
        print(f'O número {n} pertence a sequência de fibonacci')
    else:
        print(f'O número {n} não pertence a sequência de fibonacci')

except(TypeError, ValueError):
    print('O campo recebe apenas números inteiros!')