class Nodo:
	def __init__(self, valor):
		self.valor=valor
		self.siguiente=None

class lista:
	def __init__(self):
		self.tamaño=0
		self.primero=None

	def esVacia(self):
		return  self.primero==None

	def get_tam(self):
		return self.tamaño

	def encolar(self,valor):
		nuevo=Nodo(valor)
		if self.esVacia():
			self.primero=nuevo
		else:
			nuevo.siguiente=self.primero
			self.primero=nuevo
			pass
		self.tamaño += 1
		pass

	def desencolar(self):
		aux=self.primero
		if self.esVacia()==False:
			temp=self.primero.valor
			self.primero=self.primero.siguiente
			return temp
			pass
		
	def mostrar_pos(self,index):
		aux=self.primero
		if self.esVacia()==False:
			contar=0
			while(contar<=index):
				aux=aux.siguiente
				contar+=1
				pass
			return (aux.valor)
			pass
		return " "

	def mostrar(self):
		aux=self.primero
		while aux!=None:
			print(aux.valor)
			aux=aux.siguiente
			pass
