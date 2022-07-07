# 01 - Função para a organização e print da grade do jogo 
# A partir de uma lista de coordenadas e valores:
def montarGrade(grade):
  # Referências das colunas da grade (A,B,...,'I') aos índices das colunas da matriz 'grade':
  '''colunas = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'a':0, 'b':1, 
  'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8}'''
  
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



# 02 - Função para a retirada de possíveis espaços existentes na 'jogada' que poderiam 
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
        valor = valor.strip()
        valor = valor.upper()
        l[int(valor[2]) -1][let.index(valor[0])] = valor[4]
    return l

# 04 - Função que verifica se as jogadas contidas em uma lista ou inseridas pelo jogador
# estão dentro das regras do jogo:

def matriz(lin, col, val):
  m = [[val] * col for _ in range(lin)]
  return m


def verificador(col,lin,valor,a):
  
  #TRANSFORMAR AS LETRAS DA COLUNA EM SEUS RESPECTIVOS NÚMEROS
  let=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
  col = col.upper()
  for i in range(25):
    if col == let[i]:
      col = i+1


#VERIFICAR OS QUADRADOS 3X3
  passe = False

  if lin-1 <= 2 and col-1 <=2:
    for i in range(3):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 <= 2 and col-1 > 2 and col-1 <= 5:
    for i in range(3):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 <=2 and col-1 >= 6:
    for i in range(3):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 <= 2:
    for i in range(3,6):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 >=3 and col-1 <= 5:
    for i in range(3,6):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 >= 6:
    for i in range(3,6):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >=6 and col-1 <=2:
    for i in range(6,9):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 6 and col-1 >= 3 and col-1 <= 5:
    for i in range(6,9):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 6 and col-1 >= 6:
    for i in range(6,9):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break

 
  while passe == False:
    

    aux = True
    
  #VERIFICAR AS LINHAS
    for j in range(9):
      if valor == a[lin-1][j] and j!= col-1 and valor > 0:
        print("Jogada impossibilitada pela linha")
        print("Tente novamente um valor diferente de %d"%valor)
        aux = False
        break
        

  #VERIFICAR AS COLUNAS
    if aux == True:
      for i in range(9):
        if valor == a[i][col-1] and i != lin-1 and valor > 0:
          print("Jogada impossibilitada pela coluna")
          print("Tente novamente")
          aux = False
          break

    if aux:
      a[lin-1][col-1] =  valor
        

    passe = True

# 05 - Função que verifica se uma jogada coincide com uma pista:
def verificar_pista(jogada,matriz):
  jogada=jogada.upper()
  for i in range(9):
    for j in range(9):
      if jogada==matriz[i][j]:
        return False 
  return True      

# 06 - Função que verifica se uma jogada é válida:
def validar(jogada):
  col=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
  
  #Verificando os tipos da coluna, linha e valor. 
  j=jogada[0].upper()
  try:
    i=int(jogada[2])
    k=int(jogada[4])
  except:
    return False
 
# Condições pra validar a jogada:
  if  (j not in col) or i > 9 or i < 1 or k > 9 or k < 1 :
      print('Jogada Inválida.Entre um novo valor.')
      return False
  else:
      return True

# 07 - Função que deleta uma jogada requerida pelo jogador:
def deletar(a):
    # a = Dcol,lin
    col=(a[1]) 
    col=col.upper()
    lin=a[3]
   

    if verificar_pista()==True:
        matriz[n][m] = ' '
    else:
        print('Uma pista não pode ser apagada')



 

