from TabelasConfig import *

def buscaProfundidade(Tabela_inicial):

    pilha = [] # Uma lista que agira como a pilha para a pesquisa
    l = 1
    nosExpandidos = 0
    prof_max = 20
    maisProf = 0
    pilha.append(cria_node(Tabela_inicial, None, None, 0)) # Adiciona-se o nó Base
    while len(pilha) > 0:#Caso a pilha chegue a 0, nao temos solução
        node = pilha.pop(0)#take the node from the front of the queue
        if node.prof > maisProf:
            maisProf = node.prof
        if sucesso(node.estado): #se essa tabela for solução, retorna os  movimentos ate ela
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operador)
                if temp.prof <= 1:
                    break
                temp = temp.pai
            return moves,l,nosExpandidos,node.prof,maisProf
        if node.prof < prof_max:
            nosExpandidos += 1
            exp_nodes = expandir_node(node)
            pilha = exp_nodes + pilha
            if len(pilha)>l:
                l = len(pilha)

def buscaLargura(Tabela_inicial):
    fila = [] # Uma lista que agira como a pilha para a pesquisa
    maisProf = 0
    l = 1
    nosExpandidos =0
    prof_max = 20
    fila.append(cria_node(Tabela_inicial, None, None, 0)) # Adiciona-se o nó Base
    while len(fila) > 0:#Caso a pilha chegue a 0, nao temos solução
        node = fila.pop(0)#take the node from the front of the queue
        if node.prof>maisProf:
            maisProf = node.prof
        if sucesso(node.estado): #se essa tabela for solução, retorna os  movimentos ate ela
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operador)
                if temp.prof <= 1:
                    break
                temp = temp.pai
            return moves,l, nosExpandidos,node.prof,maisProf
        if node.prof < prof_max:
            nosExpandidos += 1
            exp_nodes = expandir_node(node)
            fila = fila + exp_nodes
            if len(fila)>l:
                l = len(fila)
