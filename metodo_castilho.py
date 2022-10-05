def getElemento(matriz, i, j):
	linha = matriz[i]
	elemento = linha[j]
	if type(elemento) != "<class 'int'>":
		elemento = int(elemento)
	return elemento

def processarMatriz(ArrMtx, ArrReg):
	tamanho = len(ArrMtx)
	if tamanho > 1: # One line, two columns
		novaMtx = []
		for i in range(tamanho - 1):
			novaLinha = []
			for j in range(tamanho): #there is always one more column than a line
				resultado = getElemento(ArrMtx, 1, 1) * getElemento(ArrMtx, i+1, j+1) - getElemento(ArrMtx, i+1, 1) * getElemento(ArrMtx, 1, j+1)
				novaLinha.append(resultado)
			novaMtx.append(novaLinha)
			ArrReg.append(novaMtx)
			processarMatriz(novaMtx, ArrReg)
	return ArrReg

def encontrarVariaveis(list1, n):
	if len(list1[n])>1: #encontra o tamanho da matriz dentro da lista
		n+=1
		arrayValores = encontrarVariaveis(list1, n)
	else:
		arrayValores = []
	matriz = list1[n]
	expressao = matriz[1] #escolhe uma linha arbitraria da matriz para fazer aritmetica, no caso, a primeira.
	tam = len[expressao]
	a = tam - 1
	sum = 0
	for e in range(tam-1, 1, -1): #encontra cada um dos coeficientes, exceto o primeiro da linha e o resultado (tam-1)
		if len(arrayValores) > 2:
			CoefVar = arrayValores[e] * expressao[a-1]
			sum += CoefVar
			a -= 1
	Valor = (expressao[tam] - sum)/expressao[1]
	arrayValores.append(Valor)
	return arrayValores



varNum = int(input("Numero de variaveis do sistema "))
linNum = int(input("Numero de linhas do sistema "))
if varNum == linNum:
	ArrayMatriz = []
	ArrayRegistro = []
	for i in range(varNum):
		print("Escreva os coeficientes e o resultado da linha número {}, separados por espaço: \n".format(i+1))
		strArrayLinha = input()
		ArrayLinha = strArrayLinha.split(" ")
		print(ArrayLinha) #teste
		if len(ArrayLinha) == (varNum + 1):
			ArrayMatriz.append(ArrayLinha)
		else:
			print("Sistema impossivel")
			pass
	print(ArrayMatriz) #teste
	ArrayEscalonado = processarMatriz(ArrayMatriz, ArrayRegistro)
	print(ArrayEscalonado)
	valores = encontrarVariaveis(ArrayEscalonado, 0)
else:
	print("Sistema Impossível")