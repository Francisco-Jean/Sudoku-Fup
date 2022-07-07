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

import funcoes as fun
import sys
arquivoPistas = sys.argv[1]

# Verifica se há um segundo arquivo como argumento na chamada do programa
# caso tenha, entra no modo batch
try:
    arquivoJogadas = sys.argv[2]
# caso não tenha, entra no modo interativo
except:
    pistas = fun.acessarArquivo(arquivoPistas)
    fun.montarGrade(pistas)
    jogo = True
    if len(pistas) < 81 and len(pistas) > 0:
        matriz_jogadas = pistas
        while jogo:
            jogada = input('Entre com a sua jogada no formato "<COL>,<LIN>: <NÚMERO>": ')
            lance = fun.validar(jogada)
            if not lance:
                print("Jogada invalida")
            else:
                lance = fun.verificar_pista
                jogada = fun.organizarEntradas(jogada)
                if jogada[0] == 'D' or jogada[0] == "d" and len(jogada) == 4:
                    pass
                else:
                    valida = fun.verificador(jogada[0], jogada[2], jogada[4], pistas)
                    if valida:
                        compara = True
                        if compara:
                            coluna = fun.letra_num(jogada[0])
                            linha = int(jogada[2])
                            matriz_jogadas[int(jogada[])]
                            fun.montarGrade(lista_jogadas)
                            if len(lista_jogadas) == 81:
                                jogo = False
                                print('Parabéns! Você conseguiu preencher toda a grade do jogo! :)')
                        else:
                            pass
                    else:
                        pass
    else:
        print('Configuracao de dicas invalida.')

    