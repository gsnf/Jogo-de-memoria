from TabelasConfig import *

def buscaGulosa(Tabela_inicial):
    fila = [] # Uma lista que agira como a pilha para a pesquisa
    visitados = []
    nosExpandidos = 0
    maisProf = 0
    l = 1
    prof_max = 20
    fila.append(cria_node(Tabela_inicial, None, None, 0)) # Adiciona-se o nó Base
    while len(fila) > 0:#Caso a pilha chegue a 0, nao temos solução
        node = fila.pop(0)#take the node from the front of the queue
        visitados.append(node.estado) #Guarda o estado atual para evitar repetiçoes
        if node.prof > maisProf:
            maisProf = node.prof
        fila.sort(key=sortGuloso)
        if sucesso(node.estado): #se essa tabela for solução, retorna os  movimentos ate ela
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operador)
                if temp.prof <= 1:
                    break
                temp = temp.pai
            return moves,(l + len(visitados)),nosExpandidos,node.prof,maisProf
        if node.prof < prof_max:
            exp_nodes = expandir_node(node)
            nosExpandidos += 1
            for i in exp_nodes:
                if i.estado not in visitados:
                    fila = fila + [i]
            if len(fila)>l:
                l = len(fila)

def buscaA_Estrela(Tabela_inicial):
    fila = [] # Uma lista que agira como a pilha para a pesquisa
    visitados = []
    l = 1
    nosExpandidos = 0
    prof_max = 20
    maisProf = 0
    fila.append(cria_node(Tabela_inicial, None, None, 0)) # Adiciona-se o nó Base
    while len(fila) > 0:#Caso a pilha chegue a 0, nao temos solução
        fila.sort(key=sortA_Estrela)
        node = fila.pop(0)#take the node from the front of the queue
        visitados.append(node.estado)#Guarda o estado atual para evitar repetiçoes
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
            return moves,(l + len(visitados)),nosExpandidos,node.prof,maisProf
        if node.prof < prof_max:                #se a profundidade do nó atual nao for menor que a profundidade limite,
            nosExpandidos+=1                    #nó é expandido e seus filhos sao adicionados a fila
            exp_nodes = expandir_node(node)     #e o numero de nós expandidos é aumentado
            for i in exp_nodes:
                if i.estado not in visitados:
                    fila = fila + [i]
            if len(fila)>l: #registra-se o maior tamanho da lista
                l = len(fila)