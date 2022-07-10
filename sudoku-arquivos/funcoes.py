# ARQUIVO COM TODAS AS FUNÇÕES UTILIZADAS NO PROGRAMA

# 01 - Função para a organização e print da grade do jogo 
# A partir de uma lista de coordenadas e valores:
def montarGrade(grade):

  # Print da grade formatada:
  print("     A   B   C    D   E   F    G   H   I    ")
  print('  ++---+---+---++---+---+---++---+---+---++  ')


  for i in range(9):
    print(str(i + 1) + f' || {grade[i][0]} | {grade[i][1]} | {grade[i][2]} || {grade[i][3]} |'
    f' {grade[i][4]} | {grade[i][5]} || {grade[i][6]} | {grade[i][7]} | {grade[i][8]} || ' + str(i+1))

    if i == 2 or i == 5:
      print("  ++===+===+===++===+===+===++===+===+===++ ")
    else:
      print('  ++---+---+---++---+---+---++---+---+---++ ')

  print("     A   B   C    D   E   F    G   H   I    ")



# 02 - Função para a retirada de possíveis espaços existentes na 'jogada'/'dicas' que poderiam 
# dificultar a verificação dos valores:
def organizarEntradas(data):
  if str(type(data)) == "<class 'str'>":
    return data.replace(" ", "")
  elif str(type(data)) == "<class 'list'>":
    for i in range(9):
          for j in range(9):
              data[i][j] = data[i][j].replace(" ", "")
    return data


# 03 - Função que acessa um arquivo e retorna uma matriz com as jogadas/dicas contidas nele:
def acessarArquivo(arq):
    l = [[' '] * 9 for x in range(9)]
    let = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    data = open(arq, 'r')
    for valor in data:
        if l[int(valor[2]) -1][let.index(valor[0])] == ' ':
            valor = valor.upper()
            valor = organizarEntradas(valor)
            l[int(valor[2]) -1][let.index(valor[0])] = int(valor[4])
    return l

# 04 - Função que verifica se as jogadas contidas em uma lista ou inseridas pelo jogador
# estão dentro das regras do jogo:

def verificador(col,lin,valor,a):
  #TRANSFORMAR AS LETRAS DA COLUNA EM SEUS RESPECTIVOS NÚMEROS
    let = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    col = col.upper()
    for i in range(9):
        if col == let[i]:
            col = i+1
            col = int(col)


#VERIFICAR OS QUADRADOS 3X3
    passe = True

    if lin-1 <= 2 and col-1 <=2:
        for i in range(3):
            for j in range(3):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 <= 2 and col-1 > 2 and col-1 <= 5:
        for i in range(3):
            for j in range(3,6):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 <=2 and col-1 >= 6:
        for i in range(3):
            for j in range(6,9):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >= 3 and lin-1 <= 5 and col-1 <= 2:
        for i in range(3,6):
            for j in range(3):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >= 3 and lin-1 <= 5 and col-1 >=3 and col-1 <= 5:
        for i in range(3,6):
            for j in range(3,6):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >= 3 and lin-1 <= 5 and col-1 >= 6:
        for i in range(3,6):
            for j in range(6,9):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >=6 and col-1 <=2:
        for i in range(6,9):
            for j in range(3):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >= 6 and col-1 >= 3 and col-1 <= 5:
        for i in range(6,9):
            for j in range(3,6):
                if a[i][j] == valor :
    
                    passe = False
                    break
    elif lin-1 >= 6 and col-1 >= 6:
        for i in range(6,9):
            for j in range(6,9):
                if a[i][j] == valor :
    
                    passe = False
                    break
    if passe == False:
        return False
    aux = True
  
#VERIFICAR AS LINHAS
    for j in range(9):
        if valor == a[lin-1][j] and j!= col-1:
            aux = False
            return False
        
    #VERIFICAR AS COLUNAS
    if aux == True:
        for i in range(9):
            if valor == a[i][col-1] and i != lin-1:
                aux = False
                return False
    #Adicionar o valor
    if aux:
        return True

# 05 - Função que verifica se uma jogada coincide com uma pista:
def verificar_pista(jogada,matriz):
    try:
        lin=int(jogada[3])-1
        col=letra_num(jogada[1])
        if matriz[lin][col] != ' ':
            return False 
        return True   
    except:
        return False


# 06 - Função que verifica se uma jogada é válida:
def validar(jogada):
    col=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
  
  #Verificando os tipos da coluna, linha e valor. 
    j = jogada[0].upper()
    try:
        i=int(jogada[2])
        k=int(jogada[4])
    except:
        return False
 
# Condições pra validar a jogada:
    if  (j not in col) or i > 9 or i < 1 or k > 9 or k < 1 or len(jogada) > 5:
        return False
    else:
        return True

# 07 - Função que converte as letras da coluna em números:
def letra_num(valor):
    col=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    valor = valor.upper()
    for i in range(9):
        if valor == col[i]:
            return i
            
# 08 - Função que converte os números da coluna em suas respectivas letras:
def num_letra(valor):
    col={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9}

    for c in col:
        if valor == col[c]:
            return c
            
 # 09 - Função de verificar pista alterada pra usar na função 10
def verificarpista(comando,matriz):
    linha = int(comando[2]) -1
    coluna = letra_num(comando[0])
    if matriz[linha][coluna] != ' ':
        return False
    return True   

# 10 - Função que deleta uma jogada requerida pelo jogador:
def deletar(comando,matriz, pistas):
    # comando = Dcol,lin
    lista = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    coluna1=comando[1]
    coluna1=coluna1.upper()
    coluna=letra_num(coluna1)
    try:
        linha = int(comando[3]) -1
    except:
        return False
    # matriz = grade atual
    if len(comando) == 4 and linha >= 0 and linha < 9 and (coluna1 in lista):
        if verificar_pista(comando,pistas):
            matriz[linha][coluna] = ' '
            return matriz
        else:
            return False
    else:
        return False


# 11 - Função que verifica o tamanho da matriz
def contar_tamanho(matriz):
    cont = 0
    for j in range(9):
        for i in range(9):
            if matriz[i][j] != ' ':
                cont += 1
    return cont