from BuscaForcaBruta import *
from BuscaInformada import *

Tabela1 = [4,1,2,None,5,3,6,7,8]
Tabela2 = [None,7,2,1,4,3,6,8,5]
Tabela3 = [1,2,3,4,7,5,6,8,None]
tabela = [Tabela1,Tabela2,Tabela3]



def Menu():
    while True:
        print("Tabela 1")
        printTabela(Tabela1)
        print(" ")
        print("Tabela 2")
        printTabela(Tabela2)
        print(" ")
        print("Tabela 3")
        printTabela(Tabela3)
        print(" ")
        print('Selecione uma Tabela para o Jogo ou digite 0 para Sair')
        a = int(input())
        if a == 0:
            break
        while 0<a<4:
            print("Escolha o Tipo de Busca")
            print("1 - Busca em Profundidade")
            print("2 - Busca em Largura")
            print("3 - Busca Gulosa")
            print("4 - Busca A*")
            print("5 - Todas")
            print("0 - Sair")
            a1 = int(input())
            if a1 == 0:
                a = -1
            elif a1 == 1:
                b= buscaProfundidade(tabela[a-1])
                passoaPasso(tabela[a-1],b[0])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

            elif a1 == 2:
                b= buscaLargura(tabela[a-1])
                passoaPasso(tabela[a-1],b[0])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade do Estado Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

            elif a1 == 3:
                b= buscaGulosa(tabela[a-1])
                passoaPasso(tabela[a-1],b[0])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

            elif a1 == 4:
                b = buscaA_Estrela(tabela[a-1])
                passoaPasso(tabela[a-1],b[0])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

            elif a1 == 5:
                print("Busca em Profundidade")
                b = buscaProfundidade(tabela[a - 1])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

                print("Busca em Largura")
                b = buscaLargura(tabela[a - 1])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

                print("Busca Gulosa")
                b = buscaGulosa(tabela[a - 1])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")

                print("Busca em A*")
                b = buscaA_Estrela(tabela[a - 1])
                print("Movimento: {}".format(" -> ".join(b[0])))
                print("Numero de Passos ate a Solução: {}".format(len(b[0])))
                print("Numero de nós na memoria: {}".format(b[1]))
                print("Numero de nós Expandidos: {}".format(b[2]))
                print("Profundidade Resposta: {}".format(b[3]))
                print("Profundidade Maxima: {}".format(b[4]))
                print(" ")
Menu()
