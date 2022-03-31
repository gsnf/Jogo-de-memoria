import random


Tabela_Final = [1,2,3,4,None,5,6,7,8]

def printTabela(tabela):
    print("+-----+")
    for a in range (0, len(tabela), 3):
        if tabela[a] == None:
            print("|- {} {}|".format(tabela[a+1], tabela[a+2]))
        elif tabela[a+1] == None:
            print("|{} - {}|".format(tabela[a], tabela[a + 2]))
        elif tabela[a+2] == None:
            print("|{} {} -|".format(tabela[a], tabela[a + 1]))
        else:
            print("|{} {} {}|".format(tabela[a],tabela[a+1], tabela[a+2]))
    print("+-----+")
def sucesso(a):
    if (a==Tabela_Final):
        return True
    return False

def passoaPasso(tabela, passos):
    no = tabela
    print('\n')
    printTabela(no)
    for a in passos:
        print("Movendo para {}".format(a))
        if a == "Para Baixo":
            no = move_baixo(no)
        if a == "Direita":
            no = move_dir(no)
        if a == "Para Cima":
            no = move_cima(no)
        if a == "Esquerda":
            no = move_esq(no)
        printTabela(no)
        
def move_baixo(estado):
    novo_estado = estado[:]
    index = novo_estado.index(None)
    if index not in [6, 7, 8]:
        novo_estado[index], novo_estado[index + 3] = novo_estado[index + 3], novo_estado[index]
        return novo_estado
    else:
        return None

def move_cima(estado):
    novo_estado = estado[:]
    index = novo_estado.index(None)
    if index not in [0, 1, 2]:
        novo_estado[index], novo_estado[index - 3] = novo_estado[index - 3], novo_estado[index]
        return novo_estado
    else:
        return None

def move_dir(estado):
    novo_estado = estado[:]
    index = novo_estado.index(None)
    if index not in [2, 5, 8]:
        novo_estado[index], novo_estado[index + 1] = novo_estado[index + 1], novo_estado[index]
        return novo_estado
    else:
        return None
    
def move_esq(estado):
    novo_estado = estado[:]
    index = novo_estado.index(None)
    if index not in [0, 3, 6]:
        novo_estado[index], novo_estado[index - 1] = novo_estado[index - 1], novo_estado[index]
        return novo_estado
    else:
        return None


def cria_node(estado, pai, operador, prof):
    return Node(estado, pai, operador, prof)


def expandir_node(node):
    exp_nodes = []
    exp_nodes.append(cria_node(move_cima(node.estado), node, "Para Cima", node.prof + 1))
    exp_nodes.append(cria_node(move_baixo(node.estado), node, "Para Baixo", node.prof + 1))
    exp_nodes.append(cria_node(move_esq(node.estado), node, "Esquerda", node.prof + 1))
    exp_nodes.append(cria_node(move_dir(node.estado), node, "Direita", node.prof + 1))
    exp_nodes = [node for node in exp_nodes if node.estado is not None]
    random.shuffle(exp_nodes)
    return exp_nodes

def sortGuloso(e):
    return e.custo

def sortA_Estrela(e):
    return (e.custo + e.prof)

def calcCusto(p):
    if p is None:
        return 0
    custo = 0
    for i in range (0, len(p)):
        if p[i] != Tabela_Final[i]:
            custo+=1
    return custo

class Node:
  def __init__(self, estado, pai, operador, prof):
    self.estado = estado
    self.pai = pai
    self.operador = operador
    self.prof = prof
    self.custo = calcCusto(estado)

