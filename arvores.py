class noArvore:
	def __init__(self, valor=None, esquerda=None, direita=None):
		self.valor = valor
		self.esquerda = esquerda
		self.direita = direita
	def __repr__(self):
		return '%s <- %s -> %s'%(self.esquerda and self.esquerda.valor, self.valor, self.direita and self.direita.valor)
'''
raiz = noArvore(20)
raiz.esquerda = noArvore(30)
raiz.direita = noArvore(40)

raiz.esquerda.esquerda = noArvore(15)
raiz.esquerda.direita = noArvore(25)
raiz.direita.esquerda = noArvore(35)
raiz.direita.direita = noArvore(45)

print("arvore 1:         ", raiz)
print("arvore 2: ", raiz.esquerda, raiz.direita)



def functionPreencher (raiz, counter):
	if counter <= 5:
		counter+=1
		direita = raiz.valor + 1
		esquerda = raiz.valor
		raiz.esquerda = noArvore(esquerda)
		raiz.direita = noArvore(direita)
		functionPreencher(raiz.esquerda, counter)
		functionPreencher(raiz.direita, counter)
	return raiz

def functionEscrever (raiz):
	if raiz:
		print("nivel ", raiz.valor)
		functionEscrever (raiz.esquerda)
		functionEscrever (raiz.direita)

raiz = noArvore(0)
functionPreencher(raiz, 0)
print("nivel ", raiz.direita.valor)
functionEscrever(raiz)
'''


#professor exemplo
'''
def inserirNo(raiz, no):
	if raiz is None:
		raiz = no
	elif no.valor < raiz.valor:
		if raiz.esquerda is None:
			raiz.esquerda = inserirNo(raiz, no.valor)
	elif no.valor > raiz.valor:
		if raiz.direita is None:
			raiz.direita = inserirNo(raiz, no.valor)
'''


'''
def procurarNo(raiz, valor):
	if raiz is None:
		return None:
	if raiz.valor == valor:
		return raiz
	if raiz.valor > valor:
		return procurarNo(raiz.esquerda, valor)
	if raiz.valor < valor:
		return procurarNo
'''


def inserirNo(raiz, no):
	if raiz is None:
		raiz = no
	elif no < raiz.valor:
		if raiz.esquerda is None:
			raiz.esquerda = no
		else:
			inserirNo(raiz.direita, no)
	elif no > raiz.valor:
		if raiz.direita is None:
			raiz.direita = no
		else:
			inserirNo(raiz.direita, no)


raiz = noArvore(40)
no = noArvore(30)
inserirNo(raiz, no)
#inserirNo(raiz, 20)
#inserirNo(raiz, 25)
print(raiz)

