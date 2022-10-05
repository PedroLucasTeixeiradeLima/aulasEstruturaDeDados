#import math

#s = "minha frase"
#x = 3.141529
#print("fras ", s[0:10]) # 10 e exclusivo, logo o s[10] nao aparece
#print("ase", s[-5:4])


#print("Escreva 15: {:0.6f}".format(x))

class No:
  def __init__(self, dado = 0, proximo_no = None):
    self.dado = dado
    self.proximo = proximo_no
  def __repr__(self):
    return '%s -> %s' %(self.dado, self.proximo)
class ListaEncadeada:
  def __init__(self):
    self.cabeca = None
  def __repr__(self):
    return "[" + str(self.cabeca) + "]"
def inserir_no_inicio(lista, novo_valor):
  #primeiro no
  novo_no = No(novo_valor)
  #faz com que o novo no seja a cabeca da lista
  novo_no.proximo = lista.cabeca

  #cabeca da lista referencia
  lista.cabeca = novo_no
lista = ListaEncadeada()
print("Lista esta vazia: ", lista)
inserir_no_inicio(lista, 0)
print("elementos da lista: ", lista)


for i in range(1, 23, 1):
  inserir_no_inicio(lista, i)
print("elementos da lista: ", lista)
