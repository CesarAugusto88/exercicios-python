#Exercício Torre de Hanói

#Cesar Augusto <cesarcosta.augustos@gmail.com>
#Anexos
#seg., 22 de abr. de 2019 21:38
#para pg_faria

# Mostra a matriz na tela
def disp_matriz(M):
    print()
    for linha in M:
        
        for coluna in linha:
            print("\t" + coluna + " ", end = ' ')

        print()
        
    return ''

# Função recursiva hanoi
def hanoi(n, A, B, C):
    if(n > 0):
        # Inicialmente, moveremos os n-1 primeiros discos para um pino 
        # auxiliar, em seguida, moveremos o último disco para o pino de destino.
        # E concluímos movendo os n-1 discos do pino auxiliar
        # para o pino de destino.
        hanoi(n-1, A, C, B)
        
        # As torres A, B, e C serviram para chamar a quantidade exata
        # recursiva. Porém foi feito decisões para passagem dos discos.
        if M[1][0] == '   *   ':
            M[1][0] = '   |   '
            M[3][1] = '   *   '
            
        elif M[2][0] == '  ***  ':
            M[2][0] = '   |   '
            M[3][2] = '  ***  '
                
        elif M[3][1] == '   *   ':
            M[3][1] = '   |   '
            M[2][2] = '   *   '
                
        elif M[3][0] == ' ***** ':
            M[3][0] = '   |   '
            M[3][1] = ' ***** '
                
        elif M[2][2] == '   *   ':
            M[2][2] = '   |   '
            M[3][0] = '   *   '
                
        elif M[3][2] == '  ***  ':
            M[3][2] = '   |   '
            M[2][1] = '  ***  '
                
        else:
            M[3][0] = '   |   '
            M[1][1] = '   *   '

        disp_matriz(M)
        #move disco 'n' + " de " + A + " para " + B... e depois inverte
        hanoi(n-1, C, B, A)
        
        return ''


if __name__ == '__main__':

    # Define os valores da matriz
    M = [['   |   ', '   |   ', '   |   '],
         ['   *   ', '   |   ', '   |   '],
         ['  ***  ', '   |   ', '   |   '],
         [' ***** ', '   |   ', '   |   '],
         ['---------------------------------------'],
         ['---A---------------B---------------C---']]
    print()
    
    # Mostra matriz inicial. Após será mostrado a quantidade de chamadas
    # da função recursiva na função hanoi()
    for linha in M:
        for coluna in linha:
            print("\t" + coluna + " ", end = ' ')
        print()

    # Chama função hanoi para 3 discos com torres A, B e C (C é a auxiliar)
    hanoi(3, 'A', 'B', 'C')
    print()



#Cesar Costa
#3000214

