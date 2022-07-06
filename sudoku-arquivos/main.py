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
    dicas = fun.acessarArquivo(arquivoPistas)
    dicas = fun.organizarEntradas(dicas)
    fun.montarGrade(dicas)
    jogo= True
    if len(dicas) < 81 and len(dicas) > 0:
 
        for x in dicas:
            valida = fun.validar(x)
            valida2 = fun.verificador(x[0], x[2], x[4], dicas)
            if not valida or not valida2:
                print("Configuracao de dicas invalida.")
                jogo = False
                break

        matriz_jogadas = [[]]
        if valida and valida2:
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
                        valida = verificador(jogada[0], jogada[2], jogada[4])
                        if valida:
                            compara = True
                            if compara:
                                lista_jogadas.append(jogada)
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

    