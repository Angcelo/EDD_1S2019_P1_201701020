import os

class Nodo:
	def __init__(self, valor):
		self.valor=valor
		self.siguiente=None

class Pila():
	"""docstring for Pila"""
	def __init__(self):
		self.cima=None
		self.valor=0

	def get_puntaje(self):
		return self.valor
		pass

	def esVacia(self):
		return self.cima==None
	
	def push(self,valor):
		nuevo=Nodo(valor)
		self.valor+=1
		if self.esVacia():
			self.cima=nuevo
		else:
			nuevo.siguiente=self.cima
			self.cima=nuevo
			pass

	def pop(self):
		if self.esVacia()==False:
			temp=self.cima.valor
			self.cima=self.cima.siguiente
			self.valor=self.valor-1
			return temp
		else:
			return 0

	def graficar(self):
		f=open("Pila.dot","w")
		f.write("digraph pila{\n")
		f.write("rankdir=\"LR\";\n")
		f.write("node [shape=\"record\"];\n")
		f.write("node0 [label=\"")
		aux=self.cima
		while aux!=None:
			f.write("|("+aux.valor+")")
			aux=aux.siguiente
			pass
		f.write("\",height=2.5];}")
		f.close()
		os.system("dot -Tjpg Pila.dot -o imagenPila.jpg")
