import os

class Nodo:
	def __init__(self, valor, user):
		self.puntaje=valor
		self.user=user
		self.siguiente=None

class lista:
	def __init__(self):
		self.tamaño=0
		self.primero=None

	def esVacia(self):
		return	self.primero==None

	def get_tam(self):
		return self.tamaño

	def desencolar(self):
		aux=self.primero
		if self.esVacia()==False:
			temp=self.primero.valor
			self.primero=self.primero.siguiente
			self.tamaño -= 1
			return temp
			pass

	def encolar(self,valor,user):
		nuevo=Nodo(valor,user)
		if self.esVacia():
			self.primero=nuevo
		else:
			aux=self.primero
			while aux.siguiente!=None:
				aux=aux.siguiente
				pass
			aux.siguiente=nuevo
			pass
		self.tamaño += 1
		if self.tamaño>10:
			self.desencolar()
			pass
		pass
		
	def get_user(self,index):
		aux=self.primero
		if self.esVacia()==False:
			contar=0
			while(contar<index and aux!=None):
				aux=aux.siguiente
				contar+=1
				pass
			return aux.user
			pass
		return " "

	def get_score(self,index):
		aux=self.primero
		if self.esVacia()==False:
			contar=0
			while(contar<index and aux!=None):
				aux=aux.siguiente
				contar+=1
				pass
			return aux.puntaje
			pass
		return " "

	def mostrar(self):
		aux=self.primero
		while aux!=None:
			print(aux.valor)
			aux=aux.siguiente
			pass

	def graficar(self):
		f=open("score.dot","w")
		f.write("digraph lista{\n")
		f.write("rankdir=\"LR\";\n")
		f.write("node [shape=\"record\"];\n")
		aux=self.primero
		while aux!=None:
			f.write(aux.user+str(aux.puntaje)+" [ label = \"{("+str(aux.user)+","+str(aux.puntaje)+")|\\l}\"];\n")
			aux=aux.siguiente
			pass
		aux=self.primero
		while aux!=None:
			if(aux.siguiente is not None):
				f.write(aux.user+str(aux.puntaje) + "->" +aux.siguiente.user+str(aux.siguiente.puntaje)+"\n")
			elif(aux.siguiente is None):
				f.write(aux.user+str(aux.puntaje) +"  -> \"(Null)\";\n")
				pass
			aux=aux.siguiente	
			pass
		f.write("}")
		f.close()
		os.system("dot -Tjpg score.dot -o imagenscore.jpg")
		pass
