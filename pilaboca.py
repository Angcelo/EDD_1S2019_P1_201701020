class Nodo:
	def __init__(self, valor):
		self.valor=valor
		self.siguiente=None

class Pila():
	"""docstring for Pila"""
	def __init__(self):
		self.cima=None

	def esVacia(self):
		return self.cima==None
	
	def push(self,valor):
		nuevo=Nodo(valor)
		if self.esVacia():
			self.cima=nuevo
		else:
			nuevo.siguiente=self.cima
			self.cima=nuevo

	def pop(self):
		if self.esVacia():
			temp=self.cima.valor
			self.cima=self.cima.siguiente
			return temp
			pass
		return