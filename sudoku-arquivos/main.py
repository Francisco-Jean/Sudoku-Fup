# =================================================
# ||              MEMBROS DA EQUIPE              ||
# =================================================
# |               NOME               |  MATRÍCULA |
# -------------------------------------------------
# | Francisco Jean da Silva de Sousa |   541790   |
# -------------------------------------------------
# | Levy Nascimento Oliveira         |   541800   |
# -------------------------------------------------
# | Victoria de Castro Moura         |   541801   |
# -------------------------------------------------

from copy import copy, deepcopy
from urllib.parse import parse_qs
import funcoes as fun
import sys

try:
    arquivoPistas = sys.argv[1]
except:
    print('Arquivo de pistas não encontrado.')

# Verifica se há um segundo arquivo como argumento na chamada do programa
# caso tenha, entra no modo batch
try:
    arquivoJogadas = sys.argv[2]
    pistas = ''
    # Verifica se o arquivo de pistas está correto
    try:
        # Acessa o arquivo de pistas inserido pelo usuário
        cont = 0
        pistas = fun.acessarArquivo(arquivoPistas)
        valida_pistas = True
        cont = fun.contar_tamanho(pistas)
    # Caso o arquivo de pistas esteja incorreto, invalida o arquivo
    except:
        valida_pistas = False
    if valida_pistas:
        let = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
        # Verifica se as pistas estão dentro das regras do jogo
        for i in range(9):
            for j in range(9):
                valor = pistas[i][j]
                if type(pistas[i][j]) == type(1):
                    pistas[i][j] = ' '
                    valida_pistas = fun.verificador(let[j],i+1,valor, pistas)
                    pistas[i][j] = valor
                    if not valida_pistas:
                        break
            if not valida_pistas:
                break

    # Verifica se a quantidade de pistas é menor que 81 e maior que zero e se todas as pistas são válidas
    if cont < 81 and cont > 0 and valida_pistas:
        contador = cont
        # Acessa o arquivo de jogadas inserido pelo usuário
        matriz_jogadas = fun.acessarArquivo(arquivoJogadas)
        matriz_jogadas2 = deepcopy(pistas)
        for i in range(9):
            for j in range(9):
                validador = True
                if type(matriz_jogadas[i][j]) == type(1):
                    linha = str((i + 1))
                    col = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
                    coluna = col[j]
                    valor = str(matriz_jogadas[i][j])
                    jogada = coluna + ',' + linha + ':' + valor
                    valida2 = fun.verificarpista(jogada, pistas)
                    if valida2:
                        # Verifica se a jogada inserida no arquivo está dentro das regras do jogo
                        valida3 = fun.verificador(jogada[0], int(jogada[2]), int(jogada[4]), matriz_jogadas2)
                        if valida3:
                            matriz_jogadas2[i][j] = int(valor)
                        else:
                            validador = False
                    else:
                        validador = False

                    # Caso seja encontrada uma jogada fora das regras, mostra uma mensagem de erro
                    if not validador:
                        print(f"A jogada ({jogada[0]},{jogada[2]}) = {jogada[4]} eh invalida!")
                    else:
                        contador += 1
        # Verifica se as jogadas inseridas no arquivo preenchem a grade do jogo
        if contador == 81:
            print("A grade foi preenchida com sucesso!")
        else:
            print("A grade foi nao foi preenchida!")

    else:
        print('Configuracao de dicas invalida.')




# Caso não tenha um arquivo de jogadas, entra no modo interativo:
except:
    pistas = ''
    # Verifica se o arquivo de pistas está correto
    try:
        # Acessa o arquivo de pistas inserido pelo usuário
        pistas = fun.acessarArquivo(arquivoPistas)
        fun.montarGrade(pistas)
        valida_pistas = True
        jogo = True
        cont = fun.contar_tamanho(pistas)
    # Caso o arquivo de pistas esteja incorreto, invalida o arquivo
    except:
        valida_pistas = False
    if valida_pistas:
        let = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
        # Verifica se as pistas estão dentro das regras do jogo
        for i in range(9):
            for j in range(9):
                valor = pistas[i][j]
                if type(pistas[i][j]) == type(1):
                    pistas[i][j] = ' '
                    valida_pistas = fun.verificador(let[j],i+1,valor, pistas)
                    pistas[i][j] = valor
                    if not valida_pistas:
                        break
            # Caso seja encontrada uma pista fora das regras, torna o arquivo inválido
            # e encerra o programa após a mensagem de erro
            if not valida_pistas:
                break
    # Verifica se a quantidade de pistas é menor que 81 e maior que zero e se todas as pistas são válidas
    if cont < 81 and cont > 0 and valida_pistas:
        matriz_jogadas = deepcopy(pistas)
        # Inicia o jogo
        while jogo:
            jogada = input('Entre com a sua jogada no formato "<COL>,<LIN>: <NÚMERO>": ')
            jogada = jogada.upper()
            jogada = fun.organizarEntradas(jogada)
            # Verifica se o usuário entrou com o comando de deletar jogada
            if (jogada[0] == 'D' or jogada[0] == "d") and jogada[1] != ',':
                # Verifica se o usuário está tentando deletar uma pista
                compara = fun.deletar(jogada, matriz_jogadas, pistas)
                if compara:
                    matriz_jogadas = compara
                    fun.montarGrade(matriz_jogadas)
                else:
                    print("Nao foi possivel excluir essa jogada. Tente novamente.")
            else:
                # valida se a entrada do jogador é válida
                lance = fun.validar(jogada)
                if lance:
                    compara = fun.verificarpista(jogada, pistas)
                    # Verifica se o jogador está tentando entrar com uma jogada 
                    # onde há uma pista
                    if compara:
                        # Verifica se a jogada está dentro das regras do jogo
                        aprova = fun.verificador(jogada[0], int(jogada[2]), int(jogada[4]), matriz_jogadas)
                        if aprova:
                            coluna = fun.letra_num(jogada[0])
                            linha = int(jogada[2])
                            matriz_jogadas[linha -1][coluna] = int(jogada[4])
                            fun.montarGrade(matriz_jogadas)
                            cont = fun.contar_tamanho(matriz_jogadas)
                            # Verifica se o usuário preencheu toda a grade do jogo
                            if cont == 81:
                                jogo = False
                                print('Parabéns! Você conseguiu preencher toda a grade do jogo! :)')
                        else:
                            print(f"Jogada ({jogada[0]},{jogada[2]}) = {jogada[4]} está fora das regras do jogo. Tente novamente.")
                    else:
                        print(f"A jogada ({jogada[0]},{jogada[2]}) = {jogada[4]} coincide com uma pista. Tente novamente.")
                else:
                    print("Jogada invalida. Tente Novamente.")
    else:
        print('Configuracao de dicas invalida.')

    