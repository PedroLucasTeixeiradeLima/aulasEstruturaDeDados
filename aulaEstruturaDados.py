#import math

#s = "minha frase"
#x = 3.141529
#print("fras ", s[0:10]) # 10 e exclusivo, logo o s[10] nao aparece
#print("ase", s[-5:4])


#print("Escreva 15: {:0.6f}".format(x))

class No:
  def __init__(self, dado = 0, proximo_no = None): #construtor
    self.dado = dado # O 0 sera sobrescrito nos proximos elementos. Ele apenas evita sujeira de memoria
    self.proximo = proximo_no
  def __repr__(self): #executado varias vezes
    return '%s -> %s' %(self.dado, self.proximo) #self.proximo se torna nulo, ja que nao e parametro do __repr__. self.dado é sobrescrito
class ListaEncadeada:
  def __init__(self): #construtor
    self.cabeca = None
  def __repr__(self): #executado varias vezes
    return "[" + str(self.cabeca) + "]"
def inserir_no_inicio(lista, novo_valor):
  novo_no = No(novo_valor) #define o nome do objeto (self) no construtor
  novo_no.proximo = lista.cabeca #define o self.proximo com o self sendo o novo nome do objeto

  lista.cabeca = novo_no




def inserir_depois(lista, no_anterior, novo_dado):
  novo_no = No(novo_dado)
  novo_no.proximo = no_anterior.proximo
  no_anterior.proximo = novo_no

def busca(lista, valor):
  corrente = lista.cabeca
  while corrente and corrente.dado != valor:
    corrente = corrente.proximo
  return corrente.dado

def remove(self, valor):
  assert self.cabeca, "Impossivel remover valor! Lista vazia." # nada a ser removido
  if self.cabeca.dado == valor:
    self.cabeca = self.cabeca.proximo #aponta para o proximo elemento, ignorando o valor atual
  else:
    anterior = None
    corrente = self.cabeca
    while corrente and corrente.dado != valor:
      anterior = corrente
      corrente = corrente.proximo  #aponta para o proximo elemento, ignorando o valor atual
      if corrente: #o elemento a ser removido ja e o nulo
        anterior.proximo = corrente.proximo
      else: #o elemento a ser removido e a cauda
        anterior.proximo = None



lista = ListaEncadeada() #instancia que define a cabeca da lista (self.cabeca) como nulo UMA VEZ


#print("Lista esta vazia: ", lista)
#inserir_no_inicio(lista, 0)
#print("elementos da lista: ", lista)


for i in range(23):
  inserir_no_inicio(lista, i)
print("elementos da lista: ", lista)

no_anterior = lista.cabeca
inserir_depois(lista, no_anterior, 120)
print("inserindo novo elemento depois de outro", lista)


x = busca(lista, 120)
print(x)

remove(lista, 120)
print(lista)





