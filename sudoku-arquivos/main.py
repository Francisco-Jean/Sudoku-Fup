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
import funcoes as fun
import sys
arquivoPistas = sys.argv[1]

# Verifica se há um segundo arquivo como argumento na chamada do programa
# caso tenha, entra no modo batch
try:
    arquivoJogadas = sys.argv[2]
# caso não tenha, entra no modo interativo
except:
    pistas = ''
    try:
        pistas = fun.acessarArquivo(arquivoPistas)
        fun.montarGrade(pistas)
        valida_pistas = True
        jogo = True
        atual = 0
        atual2 = 0
        cont = fun.contar_tamanho(pistas)
    except:
        valida_pistas = False
    if valida_pistas:
        let = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
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
    if cont < 81 and cont > 0 and valida_pistas:
        matriz_jogadas = deepcopy(pistas)
        while jogo:
            jogada = input('Entre com a sua jogada no formato "<COL>,<LIN>: <NÚMERO>": ')
            jogada = jogada.upper()
            jogada = fun.organizarEntradas(jogada)
            if (jogada[0] == 'D' or jogada[0] == "d") and jogada[1] != ',':
                compara = fun.deletar(jogada, matriz_jogadas, pistas)
                if compara:
                    matriz_jogadas = compara
                    fun.montarGrade(matriz_jogadas)
            else:
                lance = fun.validar(jogada)
                if lance:
                    compara = fun.verificarpista(jogada, pistas)
                    if compara:
                        aprova = fun.verificador(jogada[0], int(jogada[2]), int(jogada[4]), matriz_jogadas)
                        if aprova:
                            coluna = fun.letra_num(jogada[0])
                            linha = int(jogada[2])
                            matriz_jogadas[linha -1][coluna] = int(jogada[4])
                            fun.montarGrade(matriz_jogadas)
                            cont = fun.contar_tamanho(matriz_jogadas)
                            if cont == 81:
                                jogo = False
                                print('Parabéns! Você conseguiu preencher toda a grade do jogo! :)')
                        else:
                            print("Jogada Impossibilitada. Tente novamente.")
    else:
        print('Configuracao de dicas invalida.')

    