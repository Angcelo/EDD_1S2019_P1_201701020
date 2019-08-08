class Nodo:
	def __init__(self, valor):
		self.valor=valor
		self.siguiente=None

class lista:
	def __init__(self):
		self.tamaño=0
		self.primero=None

	def esVacia():
		return  self.primero==None

	def encolar(valor):
		nuevo=Nodo(valor)
		if esVacia():
			self.primero=nuevo
		else:
			nuevo.siguiente=self.primero
			self.primero=nuevo
			pass
		pass

	def desencolar():
		aux=self.primero
		while aux.siguiente.siguiente==None:
			aux=aux.siguiente
			pass
		temp=aux.siguiente.valor
		aux.siguiente=None
		return valor
